from bs4 import BeautifulSoup
import requests # https://www.youtube.com/watch?v=QhD015WUMxE

url = "https://royaleapi.com/blog?lang=en"

headers = {
    "User-Agent": "Mozilla/5.0"
}

update_log = requests.get(url, headers=headers)
soup = BeautifulSoup(update_log.content, "html.parser")

blogs = soup.find_all("a", href=True)

for blog in blogs:
    if blog["href"].startswith("/blog/"):
        print(blog["href"])
