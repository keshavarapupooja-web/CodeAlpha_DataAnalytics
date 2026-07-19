import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create TotalSales column
df["TotalSales"] = df["Price"] * df["Quantity"]

# Set Seaborn style
sns.set_style("whitegrid")

# ---------------- BAR CHART ----------------
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="TotalSales", data=df)
plt.title("Category Wise Sales")
plt.savefig("bar_chart.png")
plt.show()

# ---------------- PIE CHART ----------------
plt.figure(figsize=(6,6))
df.groupby("Category")["TotalSales"].sum().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales by Category")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.show()

# ---------------- HISTOGRAM ----------------
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=6)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# ---------------- LINE CHART ----------------
plt.figure(figsize=(8,5))
plt.plot(df["OrderID"], df["TotalSales"], marker="o")
plt.title("Order ID vs Total Sales")
plt.xlabel("Order ID")
plt.ylabel("Total Sales")
plt.savefig("line_chart.png")
plt.show()

# ---------------- SCATTER PLOT ----------------
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Price",
    y="Quantity",
    hue="Category",
    data=df,
    s=100
)
plt.title("Price vs Quantity")
plt.savefig("scatter_plot.png")
plt.show()

# ---------------- HEATMAP ----------------
plt.figure(figsize=(6,5))
corr = df[["Price", "Quantity", "TotalSales"]].corr()
sns.heatmap(corr, annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

print("Task 3 - Data Visualization Completed Successfully!")