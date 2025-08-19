# import libraries
from flask import Flask, render_template, request
from newsapi import NewsApiClient

# init flask app
app = Flask(__name__)

# Init news api 
newsapi = NewsApiClient(api_key='b314a7fbc26f4be5a1ef609e1c56c046')

# helper function
def get_sources_and_domains():
    all_sources = newsapi.get_sources()['sources']
    sources = []
    domains = []
    for e in all_sources:
        id = e['id']
        domain = e['url'].replace("http://", "")
        domain = domain.replace("https://", "")
        domain = domain.replace("www.", "")
        slash = domain.find('/')
        if slash != -1:
            domain = domain[:slash]
        sources.append(id)
        domains.append(domain)
    sources = ", ".join(sources)
    domains = ", ".join(domains)
    return sources, domains

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        keyword = request.form["keyword"]

        try:
            # Search news only by keyword (no sources/domains)
            related_news = newsapi.get_everything(
                q=keyword,
                language='en',
                sort_by='relevancy',
                page_size=50   # limit to avoid queryTooLong
            )

            all_articles = related_news.get('articles', [])

            return render_template("home.html", all_articles=all_articles, keyword=keyword)

        except Exception as e:
            # If API fails, show error on page instead of crashing
            return render_template("home.html", all_articles=[], keyword=keyword, error=str(e))

    else:
        try:
            # Default: show top headlines
            top_headlines = newsapi.get_top_headlines(country="in", language="en", page_size=50)
            all_headlines = top_headlines.get('articles', [])

            return render_template("home.html", all_headlines=all_headlines)

        except Exception as e:
            return render_template("home.html", all_headlines=[], error=str(e))
        
if __name__ == "__main__":
    app.run(debug=True)
