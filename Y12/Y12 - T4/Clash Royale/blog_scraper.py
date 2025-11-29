import requests
from bs4 import BeautifulSoup

URL = "https://royaleapi.com/blog?lang=en"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_blog_list():
    resp = requests.get(URL, headers=HEADERS)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    blogs = []

    # Featured
    featured = soup.select_one("#page_content > div:nth-child(4) > a")
    if featured:
        blogs.append({
            "type": "featured",
            "url": "https://royaleapi.com" + featured["href"],
            "title": featured.select_one("h2, .header").get_text(strip=True),
            "date": featured.select_one("div.content > p").get_text(strip=True),
            "cover_image": featured.select_one("img")["src"],
        })

    # Normal posts
    cards = soup.select("#page_content > div:nth-child(4) > div > a[href^='/blog/']")
    for a in cards:
        img = a.select_one("div.image img")
        cover_image = img.get("data-src") or img.get("src")

        blogs.append({
            "type": "normal",
            "url": "https://royaleapi.com" + a["href"],
            "title": a.select_one("div.content > div.header").get_text(strip=True),
            "date": a.select_one("div.content > div.description").get_text(strip=True),
            "cover_image": cover_image,
        })

    return blogs