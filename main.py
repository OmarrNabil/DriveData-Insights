# Import libraries
import pandas as pd    # used for handling data 
import seaborn as sns   # used for graphs
import matplotlib.pyplot as plt  # used to diplay graphs

# Load dataset (use only part if it's slow)
df = pd.read_csv("vehicles.csv")

# ---------------------------
# Inspect data
# ---------------------------
print("FIRST ROWS:")  # shows first 5 rows 
print(df.head())

print("\nCOLUMNS:")   # shows column names like price,year
print(df.columns)

print("\nSHAPE:")     # show the size of dataset: row: number of cars and columns: number of features
print(df.shape)

# ---------------------------
# Select important columns
# ---------------------------
df = df[['price', 'year', 'manufacturer', 'fuel', 'odometer', 'transmission']]  # keeping only the useful columns and remove unecessary data

# ---------------------------
# Clean data
# ---------------------------
# Remove missing values
df = df.dropna(subset=['price', 'year', 'manufacturer', 'fuel', 'odometer'])  # deleting rows that have missing values
# Remove unrealistic values
df = df[(df['price'] > 1000) & (df['price'] < 100000)]   # remove cheap cars less than 1000 and expensive car more than 100,000
df = df[(df['year'] > 1995) & (df['year'] <= 2023)]  # keep modern car only
df = df[(df['odometer'] > 0) & (df['odometer'] < 300000)] # remove 0 mileage and high mileage

# ---------------------------
# Visualization 1: Price vs Mileage
# ---------------------------
sns.scatterplot(x='odometer', y='price', data=df)  # make graph for price Vs mileage
plt.title("Price vs Mileage")
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()

# ---------------------------
# Visualization 2: Price vs Year
# ---------------------------
sns.scatterplot(x='year', y='price', data=df)  # make graph for price Vs year 
plt.title("Price vs Year")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

# ---------------------------
# Visualization 3: Price by Fuel Type
# ---------------------------
sns.boxplot(x='fuel', y='price', data=df)  # make graph for price by fuel type
plt.title("Price by Fuel Type")
plt.show()

# ---------------------------
# Visualization 4: Price by Manufacturer (Top 10)
# ---------------------------
top_brands = df['manufacturer'].value_counts().nlargest(10).index  # find most common manufacturers
df_top = df[df['manufacturer'].isin(top_brands)]  # Keep only top Brands

sns.barplot(x='manufacturer', y='price', data=df_top) # make graph for AVG price for each brand
plt.xticks(rotation=45) # rotates names so thy dont overlap 
plt.title("Average Price by Top Manufacturers")
plt.show()
