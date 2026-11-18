import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())

total_sales = df["Total Profit"].sum()

print("Total Sales: ", total_sales)

top = df.loc[df["Units Sold"].idxmax()]
print("Most Sales:", top["Item Type"], "with", top["Units Sold"], "units sold")

bot = df.loc[df["Units Sold"].idxmin()]
print("Less Sales : ", bot["Item Type"], "with", bot["Units Sold"], "Units Sold")


print("Average Sales :", df["Units Sold"].mean())

# group_country = df.groupby('Region')['Units Sold'].agg(['min', 'max', 'mean'])
# print(group_country)

# tabel_urut = df[['Region', 'Item Type', 'Units Sold']].sort_values(
#     by=['Region', 'Item Type']
# )
# print(tabel_urut)

total_per_item = (
    df.groupby(['Region','Item Type']) ['Units Sold'].sum().reset_index()
)

item_tertinggi = total_per_item.sort_values(
    by='Units Sold', ascending = False
).drop_duplicates(subset=['Region'])

print(item_tertinggi)