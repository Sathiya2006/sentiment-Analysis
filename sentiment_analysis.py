from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def process_news():
    news = [
        "Apple stock rises as new iPhone releases.",
        "Investors worry about market crash.",
        "Company profit increases."
    ]

    df = pd.DataFrame(news, columns=["headline"])
    df["sentiment"] = df["headline"].apply(analyze_sentiment)
    df.to_csv("news_sentiment.csv", index=False)
    print(df)

if __name__ == "__main__":
    process_news()
