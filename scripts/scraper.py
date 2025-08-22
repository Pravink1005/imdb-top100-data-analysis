import requests
import csv
import os
from get_top100 import fetch_top_movies

# 🔑 Replace with your OMDb API key
API_KEY = ""
OUTPUT_FILE = os.path.join("data", "omdb_top100.csv")

def fetch_movie_data(title, imdb_id=None):
    """
    Fetch movie details from OMDb API by IMDb ID (preferred) or title.
    """
    if imdb_id:
        url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
    else:
        url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        print(f"✅ {title} fetched")
        return {
            "Title": data.get("Title"),
            "Year": data.get("Year"),
            "Genre": data.get("Genre"),
            "Director": data.get("Director"),
            "Actors": data.get("Actors"),
            "imdbRating": data.get("imdbRating"),
            "BoxOffice": data.get("BoxOffice"),
            "Runtime": data.get("Runtime"),
            "imdbID": data.get("imdbID"),
            "imdbLink": f"https://www.imdb.com/title/{data.get('imdbID')}/"
        }
    else:
        print(f"❌ {title} → {data.get('Error')}")
        return None

def main():
    os.makedirs("data", exist_ok=True)

    movies = fetch_top_movies(limit=100)
    movie_data = []

    for m in movies:
        data = fetch_movie_data(m["title"], imdb_id=m["imdb_id"])
        if data:
            data["Rank"] = m["rank"]
            movie_data.append(data)

    if movie_data:
        fieldnames = ["Rank", "Title", "Year", "Genre", "Director", "Actors",
                      "imdbRating", "BoxOffice", "Runtime", "imdbID", "imdbLink"]
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movie_data)

        print(f"\n✅ Scraping complete! {len(movie_data)} movies saved to {OUTPUT_FILE}")
    else:
        print("❌ No movies were saved!")

if __name__ == "__main__":
    main()
