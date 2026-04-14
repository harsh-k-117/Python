import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('trends.csv')

print("First five rows of the dataset:")
print(df.head())
print()

print("Dataset description:")
print(df.describe())
print()

print("Sum of trends by month:")
print(df.groupby("month")["amount"].sum())

print("Sum of trends by category:")
print(df.groupby("category")["amount"].sum())

monthly_sales = df.groupby("month")["amount"].sum()
category_sales = df.groupby("category")["amount"].sum()

plt.plot(monthly_sales)
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

plt.pie(category_sales, labels=category_sales.index)
plt.title("Category Sales Trends")
plt.show()
