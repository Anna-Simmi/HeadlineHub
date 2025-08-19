# import libraries
import os
from flask import Flask, render_template, request
from newsapi import NewsApiClient
import traceback

# init flask app
app = Flask(__name__)

# Init news api 
API_KEY = os.environ.get('NEWSAPI_KEY')
print("DEBUG: Loaded NEWSAPI_KEY =", API_KEY)   # Debug log
newsapi = NewsApiClient(api_key=API_KEY)

# helper function
def get_sources_and_domains():
    try:
        all_sources = newsapi.get_sources()
        print("DEBUG get_sources response:", all_sources)  # Debug
        all_sources = all_sources.get('sources', [])
        sources = []
        domains = []
        for e in all_sources:
            id = e['id']
            domain = e['url'].replace("http://", "").replace("https://", "").replace("www.", "")
            slash = domain.find('/')
            if slash != -1:
                domain = domain[:slash]
            sources.append(id)
            domains.append(domain)
        sources = ", ".join(sources)
        domains = ", ".join(domains)
        return sources, domains
    except Exception as e:
        print("ERROR in get_sources_and_domains:", e)
        traceback.print_exc()
        return "", ""

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        keyword = request.form["keyword"]

        try:
            # Search news only by keyword
            related_news = newsapi.get_everything(
                q=keyword,
                language='en',
                sort_by='relevancy',
                page_size=50
            )

            print("DEBUG get_everything response:", related_news)  # Debug
            all_articles = related_news.get('articles', [])

            return render_template("home.html", all_articles=all_articles, keyword=keyword)

        except Exception as e:
            print("ERROR in POST /:", e)
            traceback.print_exc()
            return render_template("home.html", all_articles=[], keyword=keyword, error=str(e))

    else:
        try:
            # Default: show top headlines
            top_headlines = newsapi.get_top_headlines(country="in", language="en", page_size=50)
            print("DEBUG get_top_headlines response:", top_headlines)  # Debug
            all_headlines = top_headlines.get('articles', [])

            return render_template("home.html", all_headlines=all_headlines)

        except Exception as e:
            print("ERROR in GET /:", e)
            traceback.print_exc()
            return render_template("home.html", all_headlines=[], error=str(e))
        
if __name__ == "__main__":
    app.run(debug=True)
