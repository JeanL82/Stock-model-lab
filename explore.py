import pandas as pd


df = pd.read_csv("AAPL.csv",skiprows=[1,2], index_col=0,parse_dates=True)


print(df.head())
print(df.dtypes)

df['return'] = df['Close'].pct_change()
print(df[['Close','return']].head())
print(df['return'].mean())
print(df['return'].std())
