

import pandas as pd
import matplotlib.pyplot as plt  # to plot charts - visualizations


def print_symbols(count=20, symbol="*"):
    for i in range(count):
        print(symbol, end="")
    print()  # Move to a new line after the loop finishes


# A Series is Pandas' primary 1D data structure, ideal for single-variable datasets.
print_symbols(50)
print("Initialize Series from list")
print_symbols(50)
# Initialize Series from list
temperatures = pd.Series([22.5, 23.1, 21.8, 24.3, 20.9],
                         name='Daily_Temp',
                         index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(temperatures)
print_symbols(50)

# Initialize Series from dictionary
age_data = {'Alice': 19, 'Bob': 20, 'Charlie': 22, 'Diana': 21}
ages = pd.Series(age_data)
print(f"Average age: {ages.mean()}")  # Output: Average age: 20.5
print_symbols(50)

# Convert existing Series to DataFrame
print("Convert existing Series to DataFrame")
temp_df = temperatures.to_frame()
print(temp_df)  # print(temp_df.describe())
print_symbols(50)

# Initialize data frame
print("Initialize Data Frame")
data = {"category": ["Electronics", "Clothing"], "sales": [1500, 1200]}
df = pd.DataFrame(data)
print(df)

# Form a dataset
data = {
    "category": ["Electronics", "Clothing", "Books", "Electronics", "Books",
                 "Furniture", "Clothing", "Electronics", "Books", "Furniture",
                 "Electronics", "Clothing", "Books", "Furniture", "Electronics"],
    "sales": [1500, 1200, 800, 2200, 950, 1750, 1350, 2100, 890, 1900,
              2400, 1250, 920, 1800, 2300],
    "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
             "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10",
             "2024-01-11", "2024-01-12", "2024-01-13", "2024-01-14", "2024-01-15"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# save the dataset for persistence storage
df.to_csv("../../dataset/product-sales.csv", index=False)  # Saves the dataset excluding row numbers

# Load dataset
df = pd.read_csv("../../dataset/product-sales.csv")

print_symbols(50)
print("loaded dataset")
print_symbols(50)
print(df)
print_symbols(50)
# Filter data
filtered_df = df[df["sales"] > 1000]

print_symbols(50)
print("Original Data Frame before grouping")
print(df)

# Aggregate data
grouped_df1 = df.groupby("category")["sales"].sum()
print(grouped_df1)
print_symbols(100, "-")
grouped_df2 = df.groupby("category")["sales"].min()
print(grouped_df2)

grouped_sales = df.groupby("category")["sales"].sum().reset_index()  # add index to the grouped result

print_symbols(100)

# Get the count of each category
category_counts = df['category'].value_counts()

print(category_counts)

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

print(df)
print_symbols(100, "+")

# Sorting by sales in descending order
sorted_df = df.sort_values(by="sales", ascending=True)
print("Sorted by Sales (Ascending):\n", sorted_df)

print_symbols()

# Searching: Filtering products with sales greater than 1500
high_sales_df = df[df["sales"] > 1500]
print("\nHigh Sales Products (Sales > 1500):\n", high_sales_df)
print_symbols()
# Adding a new column for sales tax (assume 10% tax)
df["sales_tax"] = df["sales"] * 0.10

print("\nAdding a new column for sales tax :\n", df)

print_symbols()
# Aggregating: Computing average sales per category
avg_sales = df.groupby("category")["sales"].mean().reset_index()
print("\nAverage Sales per Category:\n", avg_sales)

# Drop rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(0)

# merging data frames

data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

data2 = {
    'Name': ['Alice', 'Bob', 'Eve'],
    'Salary': [70000, 80000, 90000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge dataframes based on 'Name' column
merged_df = pd.merge(df1, df2, on='Name', how='inner')

print(merged_df)

# Basic Plotting

# Plot a bar chart of sales
df['sales'].plot(kind='bar')

df.plot(kind="bar", x="category", y="sales", title="Sales by Category", legend=False)
plt.ylabel("Sales Amount")
plt.show()

# json conversion

# Create a product DataFrame
data = {
    'name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor'],
    'price': [1200, 800, 400, 150, 300],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'],
    'stock_amount': [10, 25, 15, 50, 20]
}

df = pd.DataFrame(data)

# Convert DataFrame to JSON
json_data = df.to_json(orient="records", indent=4)  # "records" gives list of dictionaries
print(json_data)

# Convert JSON back to DataFrame
df_from_json = pd.read_json(json_data)
print(df_from_json)

# Read JSON file into DataFrame
df = pd.read_json('../../dataset/product-sales.json')
print_symbols()
print("reading from json file into data frame\n", df)
print_symbols()
