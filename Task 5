
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Load CSV
df = pd.read_csv("sales_data.csv")

print("\n--- Dataset Preview ---")
print(df.head())
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- Dataset Summary ---")
print(df.describe())

# Sales by Product
product_sales = df.groupby("Product")["Sales"].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Sales", data=product_sales, palette="viridis")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Sales", data=region_sales, palette="coolwarm")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# Sales over Time
df["Date"] = pd.to_datetime(df["Date"])
time_sales = df.groupby("Date")["Sales"].sum().reset_index()
plt.figure(figsize=(10,6))
plt.plot(time_sales["Date"], time_sales["Sales"], marker='o')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_over_time.png")
plt.show()
