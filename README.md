# 🧠 Perception Gap+

> **“See the world differently — one story at a time.”**

Perception Gap+ is an AI-powered web application that helps users explore different **perspectives, sentiments, and trends** on any topic — and engage with a smart chatbot to ask **context-aware questions** based on real-world data.

Built for **Call2Code 2025 Hackathon**, this project demonstrates the power of combining:
- Real-time news & trends,
- Sentiment analysis, and
- Open-source LLM reasoning


## 🚀 Features (Early Prototype)

### ✅ 1. Real-Time Topic Input
Users can enter any topic such as EX: 
- BTS current news
- US H1B Visa 2025
- AI replacing jobs

### ✅ 2. News + Sentiment Dashboard
- Fetches news headlines using **NewsAPI**
- Analyzes each article’s sentiment using **VADER**
- Displays both the **headline + sentiment score**

### ✅ 3. Smart AI Chat Assistant
- Powered by **Mistral 3.2 24B Instruct (via OpenRouter)**
- Users can ask **follow-up questions** about the topic
- AI responds with **context-aware** insights using public knowledge

### ✅ 4. Streamlit-Powered UI
The entire early prototype is built using **Streamlit** for rapid development and clean layout.

- Real-time input + output flow
- Minimal UI with expandable architecture
- Fast iteration + easy deployment

> ✅ This version is **Semi working and ready for demo**!

---

## 🛠️ Tech Stack

| Layer        | Tech                                   |
|--------------|----------------------------------------|
| 🧠 LLM        | Mistral 3.2 24B (via OpenRouter)       |
| 📰 News Fetch | NewsAPI                                |
| 🧪 Sentiment  | VADER (via `vaderSentiment`)           |
| 🎨 Frontend   | Streamlit (early prototype)            |
| 🧠 Auth/Keys  | `.env` + `python-dotenv`               |
| 🛠 Backend    | Pure Python (modular architecture)     |

---

| Model                                           | Host                | Purpose                  |
| ----------------------------------------------- | ------------------- | ------------------------ |
| mistralai/mistral-small-3.2-24b-instruct-2506   | OpenRouter          | Smart contextual replies |
| VADER                                           | Local (HuggingFace) | Sentiment scoring        |
| NewsAPI                                         | NewsAPI.org         | Real-time news headlines |

## Final Frontend (Coming Soon)
The full designed UI/UX and frontend (React/Vue) will be revealed in the final presentation round.

It will include:
-Sidebar navigation
-Multi-page views
-Better visualizations (radar charts, timeline, etc.)
-Shareable insights

🔧 Current build is a prototype demonstrating the core AI functionality.

📷 Demo Screenshots: 


