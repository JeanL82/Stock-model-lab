import yfinance as yf



df = yf.download("AAPL", start = "2020-01-01")

print(df.head())