import os
import pandas as pd
import matplotlib.pyplot as plt

# Create visualization folder
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

# Total sales by product
product_sales = df.groupby("Product")["Total_Sales"].sum()

# Bar Chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/bar_chart.png")
plt.close()

# Pie Chart
plt.figure(figsize=(6, 6))
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/pie_chart.png")
plt.close()

# Print report
print("===== SALES REPORT =====")
print(f"Total Revenue: ₹{df['Total_Sales'].sum():,.2f}")
print(f"Average Sales: ₹{df['Total_Sales'].mean():,.2f}")
print(f"Highest Sale: ₹{df['Total_Sales'].max():,.2f}")
print(f"Lowest Sale: ₹{df['Total_Sales'].min():,.2f}")
print(f"Best Selling Product: {product_sales.idxmax()}")