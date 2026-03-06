import yfinance as yf
import pandas as pd

stocks = ["AAPL","MSFT","NVDA","SPY"]

data = yf.download(stocks, start="2018-01-01")["Close"]

data.to_csv("prices.csv")
