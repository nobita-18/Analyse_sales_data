import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("sales_data.csv")

# Add Revenue column
data["Revenue"] = data["Quantity"] * data["Price"]

# Total Revenue
total_revenue = data["Revenue"].sum()
print(f"Total Revenue: ₹{total_revenue}")

# Top-selling product
top_product = data.groupby("Product")["Quantity"].sum().idxmax()
print(f"Top-selling Product: {top_product}")

# Region-wise sales
region_sales = data.groupby("Region")["Revenue"].sum()
region_sales.plot(kind='bar', title='Revenue by Region')
plt.ylabel("Revenue")
plt.show()

# Monthly trend
data["Date"] = pd.to_datetime(data["Date"])
data["Month"] = data["Date"].dt.to_period("M")
monthly_sales = data.groupby("Month")["Revenue"].sum()
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.ylabel("Revenue")
plt.show()
