import requests
from bs4 import BeautifulSoup
import json
import html

def fetch_top_movies(limit=100):
    """
    Fetch IMDb Top 250 movie titles (via ld+json structured data).
    Returns up to 'limit' movies with rank, IMDb ID, and title.
    """
    url = "https://www.imdb.com/chart/top/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
        print(f"❌ Failed to fetch IMDb page (status {response.status_code})")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.select_one("script[type='application/ld+json']")

    if not script:
        print("❌ Could not find ld+json script on the page")
        return []

    data = json.loads(script.string)

    movies = []
    for i, movie in enumerate(data.get("itemListElement", []), start=1):
        if i > limit:
            break
        title = html.unescape(movie["item"].get("name"))  # decode HTML entities
        imdb_url = movie["item"].get("url")
        imdb_id = imdb_url.split("/title/")[1].strip("/") if imdb_url else None
        movies.append({
            "rank": i,
            "title": title,
            "imdb_id": imdb_id
        })

    return movies


if __name__ == "__main__":
    top100 = fetch_top_movies()
    print(f"✅ Found {len(top100)} movies")
    for movie in top100[:10]:
        print(f"{movie['rank']}. {movie['title']} ({movie['imdb_id']})")
