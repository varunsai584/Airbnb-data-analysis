import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/AB_NYC_2019.csv")

print(df.head())
print(df.info())

# Data Cleaning

df = df.dropna(subset=['price'])
df = df[df['price'] > 0]
df = df[df['price'] < 500]  # remove extreme outliers


# 1. Price Distribution

plt.figure(figsize=(8,5))
sns.histplot(df['price'], bins=50)
plt.title("Price Distribution")
plt.savefig("visuals/price_distribution.png")
plt.show()


# 2. Avg Price by Neighbourhood Group

location_price = df.groupby('neighbourhood_group')['price'].mean().sort_values()

location_price.plot(kind='bar', figsize=(8,5))
plt.title("Average Price by Location")
plt.ylabel("Price")
plt.savefig("visuals/location_price.png")
plt.show()


# 3. Room Type Analysis

room_price = df.groupby('room_type')['price'].mean()

room_price.plot(kind='bar')
plt.title("Room Type vs Price")
plt.ylabel("Price")
plt.savefig("visuals/room_type.png")
plt.show()


# 4. Reviews vs Price

plt.figure(figsize=(8,5))
sns.scatterplot(x='number_of_reviews', y='price', data=df)
plt.title("Reviews vs Price")
plt.savefig("visuals/reviews_price.png")
plt.show()


# 5. Availability Analysis

availability = df.groupby('neighbourhood_group')['availability_365'].mean()

availability.plot(kind='bar')
plt.title("Availability by Location")
plt.savefig("visuals/availability.png")
plt.show()
# 6. Top hosts
top_hosts = df['host_name'].value_counts().head(10)

top_hosts.plot(kind='bar')
plt.title("Top Hosts by Listings")
plt.savefig("visuals/top_hosts.png")
plt.show()
