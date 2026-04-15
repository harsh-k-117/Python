import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("trends.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
monthly_sales = df.groupby("month")["amount"].sum()
category_sales = df.groupby("category")["amount"].sum()
plt.plot(monthly_sales)
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
plt.pie(category_sales, labels=category_sales.index)
plt.title("Sales Distribution by Category")
plt.show()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

