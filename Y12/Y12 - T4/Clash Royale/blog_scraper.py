import requests
from bs4 import BeautifulSoup

# I learned this from YouTube and my brother helped me understand it better!

URL = "https://royaleapi.com/blog?lang=en" # URL im scraping from
HEADERS = {
    "User-Agent": "Mozilla/5.0" # so it sees a user register
}

def fetch_blog_list(): # get whats in the blog, like image, header, etc
    r = requests.get(URL, headers=HEADERS)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    all_blogs = []
    featured = soup.select_one("#page_content > div:nth-child(4) > a")

    if featured is not None:
  
        title_box = featured.select_one("h2")
        if title_box is None:
            title_box = featured.select_one(".header")


        date_box = featured.select_one("div.content > p")


        image_box = featured.select_one("img")
        if image_box:
            img_src = image_box.get("src")
        else:
            img_src = None

        all_blogs.append({ # features page (TOP PAGE/MOST RECENT)
            "type": "featured",
            "url": "https://royaleapi.com" + featured.get("href", ""),
            "title": title_box.get_text(strip=True) if title_box else None,
            "date": date_box.get_text(strip=True) if date_box else None,
            "cover_image": img_src
        })


    cards = soup.find_all("a", class_="blog-card")

    for card in cards:
        title_box = card.select_one("div.content > div.header") #getting the blog 


        date_box = card.select_one("div.content > div.description")

        image_box = card.select_one("div.image > div > img")
        if image_box:
            if image_box.get("data-src"):
                img_src = image_box.get("data-src")
            else:
                img_src = image_box.get("src")
        else:
            img_src = None

        all_blogs.append({ # normal blog posts
            "type": "normal",
            "url": "https://royaleapi.com" + card.get("href", ""),
            "title": title_box.get_text(strip=True) if title_box else None,
            "date": date_box.get_text(strip=True) if date_box else None,
            "cover_image": img_src
        })
    return all_blogs