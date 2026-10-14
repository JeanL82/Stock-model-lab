import pandas as pd


df = pd.read_csv("AAPL.csv",skiprows=1, index_col=0,parse_dates=True)


print(df.head())
print(df.dtypes)