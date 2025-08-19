import os
import traceback
import requests
from flask import Flask, render_template, request

# init flask app
app = Flask(__name__)

# API key
API_KEY = os.environ.get("NEWSAPI_KEY")
print("DEBUG: Loaded NEWSAPI_KEY =", API_KEY)

BASE_URL = "https://newsapi.org/v2"

def fetch_news(endpoint, params):
    """Helper function to fetch news and log raw response"""
    try:
        params["apiKey"] = API_KEY
        url = f"{BASE_URL}/{endpoint}"
        resp = requests.get(url, params=params, timeout=10)
        print(f"DEBUG Request URL: {resp.url}")
        print(f"DEBUG Status Code: {resp.status_code}")
        print(f"DEBUG Raw Response (first 500 chars): {resp.text[:500]}")
        resp.raise_for_status()  # raise HTTP errors
        return resp.json()
    except Exception as e:
        print("ERROR in fetch_news:", e)
        traceback.print_exc()
        return {"status": "error", "message": str(e)}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        keyword = request.form["keyword"]

        related_news = fetch_news("everything", {
            "q": keyword,
            "language": "en",
            "sortBy": "relevancy",
            "pageSize": 50
        })

        if related_news.get("status") == "ok":
            all_articles = related_news.get("articles", [])
            return render_template("home.html", all_articles=all_articles, keyword=keyword)
        else:
            return render_template("home.html", all_articles=[], keyword=keyword, error=related_news.get("message"))

    else:
        top_headlines = fetch_news("top-headlines", {
            "country": "in",
            "language": "en",
            "pageSize": 50
        })

        if top_headlines.get("status") == "ok":
            all_headlines = top_headlines.get("articles", [])
            return render_template("home.html", all_headlines=all_headlines)
        else:
            return render_template("home.html", all_headlines=[], error=top_headlines.get("message"))

if __name__ == "__main__":
    app.run(debug=True)
