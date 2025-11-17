import requests
from bs4 import BeautifulSoup

# I watched a Youtube video to make this, then i sat down with my brother who does this stuff for a living for about 2 hours and he explained alot of it to me!

URL = "https://royaleapi.com/blog?lang=en"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def fetch_blog_list():
    resp = requests.get(URL, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    blogs = []

    featured_card = soup.select_one("#page_content > div:nth-child(4) > a")
    if featured_card:
        title_tag = featured_card.select_one("h2, .header")
        date_tag = featured_card.select_one("div.content > p")
        img_tag = featured_card.select_one("img")

        blogs.append({
            "type": "featured",
            "url": f"https://royaleapi.com{featured_card['href']}",
            "title": title_tag.get_text(strip=True) if title_tag else None,
            "date": date_tag.get_text(strip=True) if date_tag else None,
            "cover_image": img_tag["src"] if img_tag else None,
        })


    normal_cards = soup.select("#page_content > div:nth-child(4) > div > a[href^='/blog/']")

    for a in normal_cards:
        title_tag = a.select_one("div.content > div.header")
        date_tag = a.select_one("div.content > div.description")
        img_tag = a.select_one("div.image > div > img")
        cover_image = img_tag.get("data-src") or img_tag.get("src") if img_tag else None

        blogs.append({
            "type": "normal",
            "url": f"https://royaleapi.com{a['href']}",
            "title": title_tag.get_text(strip=True) if title_tag else None,
            "date": date_tag.get_text(strip=True) if date_tag else None,
            "cover_image": cover_image,
        })


    return blogs
