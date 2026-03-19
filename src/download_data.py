import os
import yfinance as yf
import pandas as pd


def download_price_data(stocks, start_date="2018-01-01", output_path="data/prices.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    data = yf.download(stocks, start=start_date)["Close"]

    if data.empty:
        raise ValueError("No data was downloaded. Please check ticker symbols or internet connection.")

    data.to_csv(output_path)
    print(f"Price data saved to: {output_path}")
    return data


if __name__ == "__main__":
    stocks = ["AAPL", "MSFT", "NVDA", "SPY"]
    download_price_data(stocks)
    
