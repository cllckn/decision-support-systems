# This script reads the dataset, performs basic analysis, converts it to JSON,
# and visualizes the age distribution using a histogram.

import pandas as pd
import json
import matplotlib.pyplot as plt

# Task 1: Download and Load the Dataset
file_path = "../../../dataset/Employee.csv"  # Ensure this file is downloaded and placed correctly

df = pd.read_csv(file_path)

# Task 2: Perform Data Analysis
# 1. Calculate min, max, and average age
min_age = df["Age"].min()
max_age = df["Age"].max()
avg_age = df["Age"].mean()
print(f"Minimum Age: {min_age}, Maximum Age: {max_age:.2f}, Average Age: {avg_age:.2f}")

# 2. Average age by gender
avg_age_by_gender = df.groupby("Gender")["Age"].mean()
print("Average Age by Gender:\n", avg_age_by_gender)

# 3. Count employees by education group
education_counts = df["Education"].value_counts()
print("Employee Count by Education Level:\n", education_counts)

# Task 3: Convert Data to JSON
json_data = df.to_json(orient="records", indent=4)
with open("employee_data.json", "w") as json_file:
    json_file.write(json_data)

# Additional Challenge: Visualizing Age Distribution
plt.figure(figsize=(8, 5))  # Form a figure with size 8x5 inches

plt.hist(df["Age"], bins=10, edgecolor='black', alpha=0.7)  # Form a histogram of ages
# bins=10: Divides the age range into 10 bins
# edgecolor='black': Adds black borders to each bin
# alpha=0.7: Makes bars slightly transparent for a better visual effect

plt.xlabel("Age")  # Label for x-axis
plt.ylabel("Frequency")  # Label for y-axis
plt.title("Age Distribution of Employees")  # Title for the histogram

plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines for better readability
# axis='y': Apply grid only to the y-axis
# linestyle='--': Use dashed lines
# alpha=0.7: Make grid lines slightly transparent
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add horizontal grid lines for better readability

plt.show()  # Display the histogram
