# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (use only part if it's slow)
df = pd.read_csv("vehicles.csv")

# ---------------------------
# Inspect data
# ---------------------------
print("FIRST ROWS:")
print(df.head())

print("\nCOLUMNS:")
print(df.columns)

print("\nSHAPE:")
print(df.shape)

# ---------------------------
# Select important columns
# ---------------------------
df = df[['price', 'year', 'manufacturer', 'fuel', 'odometer', 'transmission']]

# ---------------------------
# Clean data
# ---------------------------
# Remove missing values
df = df.dropna(subset=['price', 'year', 'manufacturer', 'fuel', 'odometer'])
# Remove unrealistic values
df = df[(df['price'] > 1000) & (df['price'] < 100000)]
df = df[(df['year'] > 1995) & (df['year'] <= 2023)]
df = df[(df['odometer'] > 0) & (df['odometer'] < 300000)]

# ---------------------------
# Visualization 1: Price vs Mileage
# ---------------------------
sns.scatterplot(x='odometer', y='price', data=df)
plt.title("Price vs Mileage")
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()

# ---------------------------
# Visualization 2: Price vs Year
# ---------------------------
sns.scatterplot(x='year', y='price', data=df)
plt.title("Price vs Year")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

# ---------------------------
# Visualization 3: Price by Fuel Type
# ---------------------------
sns.boxplot(x='fuel', y='price', data=df)
plt.title("Price by Fuel Type")
plt.show()

# ---------------------------
# Visualization 4: Price by Manufacturer (Top 10)
# ---------------------------
top_brands = df['manufacturer'].value_counts().nlargest(10).index
df_top = df[df['manufacturer'].isin(top_brands)]

sns.barplot(x='manufacturer', y='price', data=df_top)
plt.xticks(rotation=45)
plt.title("Average Price by Top Manufacturers")
plt.show()
