import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\kulka\OneDrive\Desktop\Codes and Stuff\car_prices.csv')

print("Top 10 Sales Records:")
print(df.head(10))

model_input = input("Enter vehicle model (e.g., BMW, Audi): ").strip()

model_data = df[df['make'].str.lower() == model_input.lower()]

model_data['saledate'] = pd.to_datetime(model_data['saledate'], errors='coerce')

model_data = model_data.dropna(subset=['saledate', 'sellingprice'])

model_data = model_data.sort_values('saledate')

plt.figure(figsize=(10, 5))
plt.plot(model_data['saledate'], model_data['sellingprice'], marker='o')
plt.title(f'{model_input} Sales Over Time')
plt.xlabel('Sale Date')
plt.ylabel('Selling Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
