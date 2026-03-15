from streamlit_autorefresh import st_autorefresh
import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.news_collector import fetch_news

st.set_page_config(page_title="AI News Intelligence", layout="wide")

st.title("🧠 AI News Intelligence Dashboard")

# refresh every 2 minutes
st_autorefresh(interval=120000, key="news_refresh")

news = fetch_news()

df = pd.DataFrame(news)

if df.empty:
    st.warning("No news found.")

else:

    # SIDEBAR
    st.sidebar.header("Filters")

    # 🔎 SEARCH FEATURE
    search_topic = st.sidebar.text_input("🔎 Search News")

    topic_filter = st.sidebar.selectbox(
        "Filter by Topic",
        ["All"] + list(df["Topic"].unique()),
        key="topic_filter"
    )

    # APPLY FILTERS
    if topic_filter != "All":
        df = df[df["Topic"] == topic_filter]

    if search_topic:
        df = df[
            df["Title"].str.contains(search_topic, case=False) |
            df["Topic"].str.contains(search_topic, case=False) |
            df["Source"].str.contains(search_topic, case=False)
        ]

    # NEWS SECTION
    st.subheader("📰 Latest News")

    if df.empty:
        st.warning(f"⚠️ No news articles found for '{search_topic}'. Try another keyword.")

    else:

        for _, row in df.iterrows():

            st.markdown(f"### {row['Title']}")
            st.write("Source:", row["Source"])
            st.write("Topic:", row["Topic"])
            st.write("Sentiment:", row["Sentiment"])
            st.write("Fake News Probability:", row["Fake News %"], "%")
            st.markdown(f"[Read Full Article]({row['URL']})")

            st.divider()

        # SENTIMENT CHART
        st.subheader("📊 Sentiment Analysis")
        st.bar_chart(df["Sentiment"].value_counts())

        # 🔥 TRENDING TOPICS
        st.subheader("🔥 Trending Topics")

        topic_counts = df["Topic"].value_counts()

        fig_topics = px.bar(
            x=topic_counts.index,
            y=topic_counts.values,
            labels={"x": "Topic", "y": "Number of News Articles"},
            title="Trending News Topics"
        )

        st.plotly_chart(fig_topics)

        # MARKET SENTIMENT PREDICTION
        st.subheader("📈 Market Sentiment Prediction")

        positive_count = len(df[df["Sentiment"] == "Positive"])
        negative_count = len(df[df["Sentiment"] == "Negative"])
        neutral_count = len(df[df["Sentiment"] == "Neutral"])

        total = positive_count + negative_count + neutral_count

        if total > 0:

            market_score = (positive_count - negative_count) / total

            if market_score > 0.2:
                prediction = "📈 Bullish Market Trend"
            elif market_score < -0.2:
                prediction = "📉 Bearish Market Trend"
            else:
                prediction = "➡️ Stable Market"

            st.metric("Market Sentiment Score", round(market_score, 2))
            st.success(prediction)

        else:
            st.warning("Not enough news data.")

        # STOCK MARKET SECTION
        st.subheader("📊 Stock Market vs News Sentiment")

        stock_symbol = st.selectbox(
            "Select Stock",
            ["AAPL", "TSLA", "GOOGL", "MSFT", "AMZN"],
            key="stock_selector"
        )

        stock_data = yf.download(stock_symbol, period="7d", interval="1h")

        if not stock_data.empty:

            if hasattr(stock_data.columns, "levels"):
                stock_data.columns = stock_data.columns.get_level_values(0)

            fig = px.line(
                stock_data,
                x=stock_data.index,
                y="Close",
                title=f"{stock_symbol} Stock Price"
            )

            st.plotly_chart(fig)

        else:
            st.warning("Stock data not available.")

        # NEWS IMPACT SCORE
        st.subheader("🧠 News Sentiment Impact Score")

        positive = len(df[df["Sentiment"] == "Positive"])
        negative = len(df[df["Sentiment"] == "Negative"])

        impact_score = positive - negative

        st.metric("Market Impact Score", impact_score)

        if impact_score > 3:
            st.success("📈 Strong Positive Market Sentiment")

        elif impact_score < -3:
            st.error("📉 Strong Negative Market Sentiment")

        else:
            st.info("➡️ Neutral Market Sentiment")