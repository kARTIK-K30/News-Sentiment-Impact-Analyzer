# 🧠 AI News Sentiment Impact Analyzer

An AI-powered dashboard that collects live news, analyzes sentiment, detects possible fake news, identifies topics, and predicts potential market impact.
The dashboard also visualizes stock market data and compares it with overall news sentiment.

This project demonstrates how **Natural Language Processing (NLP)** and **data visualization** can be combined to extract insights from news data.

---

# 📌 Project Overview

The **AI News Sentiment Impact Analyzer** automatically collects the latest news articles using a news API, processes the text, and performs multiple AI-based analyses such as:

* News sentiment detection
* Topic classification
* Fake news probability estimation
* Market sentiment prediction
* Stock price visualization

The results are displayed in an interactive dashboard built using **Streamlit**, allowing users to easily explore news insights.

---

# 🚀 Features

### 📰 Live News Collection

Fetches the latest news articles from an external news API.

### 😊 Sentiment Analysis

Determines whether each news article has a **Positive**, **Negative**, or **Neutral** sentiment.

### 🧠 Topic Detection

Automatically categorizes news into topics such as:

* Technology
* Business
* Politics
* Finance
* General News

### 🚨 Fake News Probability

Estimates the likelihood that a news article could be misleading or fake.

### 📊 Sentiment Visualization

Displays sentiment distribution using charts to understand overall news tone.

### 📈 Market Sentiment Prediction

Calculates a market sentiment score based on news sentiment to indicate whether the market outlook is:

* Bullish
* Bearish
* Stable

### 📉 Stock Market Visualization

Fetches real-time stock data using **yfinance** and displays price movements using interactive graphs built with **Plotly**.

### 🔎 Interactive Filters

Users can filter news articles by topic using sidebar controls.

---

# 🏗 Project Architecture

```
News-Sentiment-Impact-Analyzer
│
├── dashboard
│   └── app.py
│
├── utils
│   └── news_collector.py
│
├── models
│   ├── sentiment_model.py
│   ├── fake_news_detector.py
│   └── topic_detector.py
│
├── data
│
├── requirements.txt
└── README.md
```

---

# ⚙️ How the System Works

The project workflow consists of multiple stages.

## 1️⃣ News Collection

The system retrieves news articles using a news API.

The collected data includes:

* Article title
* Source
* URL
* Description
* Image

This step is handled in:

```
utils/news_collector.py
```

---

## 2️⃣ Sentiment Analysis

Each news article title is analyzed using NLP techniques to determine its sentiment.

Possible outputs:

* Positive
* Negative
* Neutral

This logic is implemented in:

```
models/sentiment_model.py
```

---

## 3️⃣ Topic Detection

The system categorizes articles into topics based on keywords.

Example topics include:

* Technology
* Finance
* Politics
* Business

Implemented in:

```
models/topic_detector.py
```

---

## 4️⃣ Fake News Detection

A probability score is generated indicating the likelihood of fake news.

Currently this is a heuristic-based approach but can be replaced with a machine learning model.

Implemented in:

```
models/fake_news_detector.py
```

---

## 5️⃣ Data Visualization

The processed news data is visualized through an interactive dashboard created using **Streamlit**.

Visual components include:

* News article cards
* Sentiment distribution charts
* Market sentiment indicators
* Stock price graphs

---

# 📊 Market Sentiment Algorithm

Market sentiment is calculated using:

```
Market Score = (Positive News - Negative News) / Total News
```

Interpretation:

| Score Range | Market Prediction |
| ----------- | ----------------- |
| > 0.2       | Bullish Market    |
| < -0.2      | Bearish Market    |
| Otherwise   | Stable Market     |

---

# 🛠 Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Core programming language |
| **Streamlit** | Interactive dashboard     |
| **Pandas**    | Data processing           |
| **Plotly**    | Data visualization        |
| **yfinance**  | Stock market data         |
| Requests      | API communication         |

---

# 💻 Installation Guide

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/AI-News-Sentiment-Impact-Analyzer.git
```

---

### 2️⃣ Navigate to the Project

```
cd AI-News-Sentiment-Impact-Analyzer
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Dashboard

```
streamlit run dashboard/app.py
```

---

# 📷 Dashboard Preview

The dashboard includes:

* News feed
* Topic filtering
* Sentiment charts
* Market prediction
* Stock price visualization

---

# 🔮 Future Improvements

Possible enhancements for the project:

* Machine learning based fake news detection
* Advanced NLP models
* News clustering
* Trending topic analysis
* Real-time news updates
* Social media sentiment integration
* Deployment as a public web application

---

# 📚 Learning Outcomes

This project demonstrates:

* Data collection from APIs
* Natural Language Processing basics
* Data visualization techniques
* Dashboard development
* Sentiment-driven analytics

---

# 👨‍💻 Author

**Kartik Kumar**

AI & Data Science Enthusiast

---

# ⭐ If You Like This Project

Please consider giving the repository a **st**
