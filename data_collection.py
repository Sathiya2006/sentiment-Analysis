import yfinance as yf
import pandas as pd

def get_stock_data(symbol, period="1y"):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    df.to_csv("stock_data.csv")
    print("Stock data downloaded!")
    return df

if __name__ == "__main__":
    get_stock_data("AAPL")  # You can change this to any stock

