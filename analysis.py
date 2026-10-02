import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Create Sales column
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Create Profit column
df["Profit"] = (df["Quantity"] * df["Unit_Price"]) - (
    df["Quantity"] * df["Unit_Cost"]
)


# =========================================================
# 1. Total Orders
# =========================================================
print("1. Total Orders =", df["Order_ID"].nunique())
# Answer: 839


# =========================================================
# 2. Total Units Sold
# =========================================================
print("2. Total Units =", df["Quantity"].sum())
# Answer: 4556


# =========================================================
# 3. Total Cities
# =========================================================
print("3. Total Cities =", df["City"].nunique())
# Answer: 4


# =========================================================
# 4. Total Categories
# =========================================================
print("4. Total Categories =", df["Category"].nunique())
# Answer: 5


# =========================================================
# 5. Customer Type Count
# =========================================================
print("\n5. Customer Type:")
print(df["Customer_Type"].value_counts())
# Normal = 443
# Member = 396


# =========================================================
# 6. Total Sales
# =========================================================
print("\n6. Total Sales =", df["Sales"].sum())
# Answer: 255547


# =========================================================
# 7. Sales by City
# =========================================================
print("\n7. Sales by City:")
print(df.groupby("City")["Sales"].sum().sort_values(ascending=False))

# Hyderabad        71358
# Visakhapatnam    70981
# Vijayawada       58186
# Warangal         55022


# =========================================================
# 8. Sales by Category
# =========================================================
print("\n8. Sales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# Personal Care    105940
# Beverage          75250
# Grocery           33155
# Dairy             24677
# Snacks            16525


# =========================================================
# 9. Sales by Product
# =========================================================
print("\n9. Sales by Product:")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

# Shampoo     78960
# Tea         48250
# Rice        30395
# Juice       27000
# Soap        26980
# Milk        24677
# Biscuits    16525
# Oil          2760


# =========================================================
# 10. Most Used Payment Method
# =========================================================
print("\n10. Most Used Payment Method:")
print(df["Payment_Method"].value_counts())

# Wallet    223
# Cash      216
# UPI       212
# Card      188


# =========================================================
# 11. Sales by Branch
# =========================================================
print("\n11. Sales by Branch:")
print(df.groupby("Branch")["Sales"].sum().sort_values(ascending=False))

# A    71358
# D    70981
# C    58186
# B    55022


# =========================================================
# 12. Total Profit
# =========================================================
print("\n12. Total Profit =", df["Profit"].sum())
# Answer: 79544


# =========================================================
# 13. Profit by Category
# =========================================================
print("\n13. Profit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# Personal Care    34910
# Beverage         23075
# Grocery           8550
# Dairy             6809
# Snacks            6200


# =========================================================
# 14. Top 5 Products
# =========================================================
print("\n14. Top 5 Products:")
print(
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Shampoo    78960
# Tea        48250
# Rice       30395
# Juice      27000
# Soap       26980


# =========================================================
# 15. Average Order Value
# =========================================================
print(
    "\n15. Average Order Value =",
    df["Sales"].sum() / df["Order_ID"].nunique()
)

# Answer: 304.5852205
# Approximately: 304.59