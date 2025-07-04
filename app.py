import streamlit as st
import requests
import os
from dotenv import load_dotenv
from utils.fetch_news import fetch_news
from utils.analyze_sentiment import get_sentiment

# Load API keys
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# HuggingFace assistant
import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_ai_response(question, topic):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-small-3.2-24b-instruct-2506:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who answers questions using news and real-world trends."},
            {"role": "user", "content": f"Topic: {topic}\nQuestion: {question}"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        res_json = response.json()
        print("🧪 OpenRouter response:", res_json)
        return res_json['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("❌ OpenRouter Error:", e)
        return "Sorry, the assistant is currently unavailable."


# Streamlit UI
st.set_page_config(page_title="Perception Gap+", layout="wide")
st.title("🧠 Perception Gap+")
st.subheader("Explore how the world views your topic + Ask our AI assistant")

topic = st.text_input("Enter a topic (e.g., US H1B Visa 2025)")

if topic:
    # News + Sentiment
    st.markdown("### 📰 News Headlines & Sentiment")
    articles = fetch_news(topic)

    if not articles:
        st.warning("No relevant news found. Try a simpler topic.")
    else:
        for art in articles:
            st.write("------")
            st.subheader(art["title"])
            st.caption(f"Source: {art['source']['name']}")
            st.write(art["description"])
            sentiment = get_sentiment(art["description"] or "")
            score = sentiment['compound']
            st.text(f"Sentiment Score: {score:.2f}")

    # Chat Assistant
    st.markdown("### 💬 Ask the AI Assistant")
    user_question = st.text_input("Ask a question about this topic")

    if user_question:
        with st.spinner("Thinking..."):
            response = get_ai_response(user_question, topic)
        st.success("🤖 " + response)
