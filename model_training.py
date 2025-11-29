import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model():
    stock = pd.read_csv("stock_data.csv")
    news = pd.read_csv("news_sentiment.csv")

    stock["sentiment"] = news["sentiment"].mean()

    stock["target"] = stock["Close"].shift(-1)
    stock.dropna(inplace=True)

    X = stock[["Close", "sentiment"]]
    y = stock["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)

    print("Model trained!")
    return model

if __name__ == "__main__":
    train_model()
