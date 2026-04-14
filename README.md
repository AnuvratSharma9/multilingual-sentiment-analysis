# 🌐 IN Multilingual Sentiment Analysis System

> Analyze sentiment across Indian languages — giving voice to the non-English speaker.

---

## 📌 Overview

A multilingual NLP tool that detects the emotional tone of text written in Indian languages. It translates input text to English, runs sentiment analysis, and returns the result translated back into the target language.

Built with **Gradio** and hosted on **Hugging Face Spaces**.

🔗 [Live Demo](https://huggingface.co/spaces/bolt77/multi_lingual_sentiment_checker)

---

## 🧠 How It Works# 🌐 IN Multilingual Sentiment Analysis System

> Analyze sentiment across Indian languages — giving voice to the non-English speaker.

---

## 📌 Overview

A multilingual NLP tool that detects the emotional tone of text written in Indian languages. It translates input text to English, runs sentiment analysis, and returns the result translated back into the target language.

Built with **Gradio** and hosted on **Hugging Face Spaces**.

🔗 [Live Demo](https://huggingface.co/spaces/bolt77/multi_lingual_sentiment_checker)

---

## 🧠 How It Works

## ✨ Features

- **Multilingual Input** — accepts text in Indian regional languages
- **Sentiment Detection** — classifies as POSITIVE, NEGATIVE, or NEUTRAL with a confidence score
- **Translation Pipeline** — translates to English for analysis, then back to target language
- **Simple UI** — clean Gradio interface, no coding required to use

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| UI Framework | Gradio |
| Sentiment Model | `distilbert-base-uncased-finetuned-sst-2-english` |
| Translation Model | Helsinki-NLP / OPUS-MT (~2.46GB) |
| Hosting | Hugging Face Spaces (Free Tier) |
| Language | Python |

---

## 🚀 Use Cases

### 🛒 E-commerce
Analyze product reviews written in Hindi, Tamil, Bengali, and other regional languages.

### 📱 Social Media Monitoring
Track brand reputation and public sentiment on Hindi/Tamil Twitter or regional platforms.

### 🏥 Healthcare & Government
Process patient feedback or citizen grievances submitted in regional languages.

### 📞 Customer Support
Auto-detect negative sentiment in support tickets written in any Indian language.

### 📰 News & Media
Gauge public reaction to regional language news stories.

---

## 💡 The Problem It Solves

Most sentiment analysis pipelines are English-only. In India, the majority of ~1.4 billion people communicate in Hindi, Tamil, Telugu, Bengali, Marathi, Punjabi, and more — often in:
- Native scripts (हिंदी, தமிழ், తెలుగు)
- Transliterated form ("yaar ye product bakwaas hai")
- Code-switched mixed language ("mujhe bahut acha laga 😊")

---

## ⚙️ Running Locally

```bash
git clone https://huggingface.co/spaces/bolt77/multi_lingual_sentiment_checker
pip install -r requirements.txt
python app.py
```

> ⚠️ Note: Translation model is ~2.46GB. Ensure 8GB+ RAM before running locally.

---

## 📊 Example

| Input | Source | Target | Sentiment | Translation |
|---|---|---|---|---|
| Hi there I wanted to see you | English | Hindi | 😊 POSITIVE (1.0) | हाय वहाँ मैं तुम्हें देखना चाहता था |

---


*Built with ❤️ for linguistic inclusion in AI*
