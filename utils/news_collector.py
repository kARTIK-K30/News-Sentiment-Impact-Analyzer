import requests

from models.sentiment import analyze_sentiment
from models.topic_detector import detect_topic
from models.fake_news_detector import fake_probability


API_KEY = "YOUR NEWSAPI KEY"


def fetch_news():

    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    if "articles" not in data:
        print(data)
        return []

    articles = data["articles"]

    news_list = []

    for a in articles:

        title = a.get("title","No title")
        source = a["source"]["name"] if a.get("source") else "Unknown"
        url = a.get("url","#")
        image = a.get("urlToImage",None)

        sentiment = analyze_sentiment(title)
        topic = detect_topic(title)
        fake_score = fake_probability(title)

        news_list.append({
            "Title": title,
            "Source": source,
            "Topic": topic,
            "Sentiment": sentiment,
            "Fake News %": fake_score,
            "URL": url,
            "Image": image
        })

    return news_list
