import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=relevancy&language=en&pageSize=5&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            print("❌ NewsAPI error:", response.status_code, response.text)
            return []
    except Exception as e:
        print("❌ Exception fetching news:", e)
        return []
