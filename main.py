import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())

total_sales = df["Total Profit"].sum()

print("Total Sales: ", total_sales)