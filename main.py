# Project 1: Used Car Price Analysis

# 1️⃣ Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2️⃣ Load dataset
df = pd.read_csv("final_cars_datasets.csv")

# Remove unnecessary column if exists
df = df.drop(columns=['Unnamed: 0'], errors='ignore')

# 3️⃣ Show first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# 4️⃣ Show columns
print("\nCOLUMNS:")
print(df.columns)

# 5️⃣ Select important columns
df = df[['price', 'year', 'mark', 'fuel', 'mileage', 'transmission']]

print("\nAFTER SELECTING IMPORTANT COLUMNS:")
print(df.head())

# 6️⃣ Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# 7️⃣ Remove missing values
df = df.dropna()

# 8️⃣ Clean unrealistic values
df = df[(df['price'] > 1000) & (df['price'] < 100000)]
df = df[(df['mileage'] > 0) & (df['mileage'] < 300000)]

print("\nFINAL CLEANED DATA:")
print(df.head())

# 📊 VISUALIZATIONS

# Price vs Mileage
plt.figure()
sns.scatterplot(x='mileage', y='price', data=df)
plt.title("Price vs Mileage")
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()

# Price vs Year
plt.figure()
sns.scatterplot(x='year', y='price', data=df)
plt.title("Price vs Year")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

# Price by Fuel Type
plt.figure()
sns.boxplot(x='fuel', y='price', data=df)
plt.title("Price by Fuel Type")
plt.show()

# Average Price by Brand
top_brands = df['mark'].value_counts().nlargest(10).index
df_top = df[df['mark'].isin(top_brands)]

plt.figure()
sns.barplot(x='mark', y='price', data=df_top)
plt.xticks(rotation=45)
plt.title("Average Price by Top Brands")
plt.show()
