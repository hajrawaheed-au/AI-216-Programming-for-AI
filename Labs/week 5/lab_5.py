# Problem 1
import numpy as np

sensor_data = np.array([
    [12, 15, 14, 10, 13],
    [20, 22, 19, 18, 21],
    [30, 28, 27, 29, 31],
    [25, 24, 26, 23, 22]
])

avg_per_machine=np.mean(sensor_data,axis=1)
print("avg per machine is:",avg_per_machine)

max_per_column= np.max(sensor_data, axis=0)
print("maximum value percolumn is: ",max_per_column)

normalized= sensor_data / max_per_column
print("normalized value is:",normalized)

for i in range(len(avg_per_machine)):
    if avg_per_machine[i] > 20:
        print("Machine", i+1)

reshaped_matrix=sensor_data.reshape(2,10)
print(reshaped_matrix)

#Problem 2

import numpy as np

matrix1 = np.random.randint(1, 51, (3, 3))
matrix2 = np.random.randint(1, 51, (3, 3))

print("Matrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)

matrix_mult = matrix1 @ matrix2
print("\nMatrix Multiplication (Matrix1 @ Matrix2):\n", matrix_mult)

element_wise = matrix1 * matrix2
print("\nElement-wise Multiplication (Matrix1 * Matrix2):\n", element_wise)

greater_than_100 = matrix_mult[matrix_mult > 100]
print("\nElements > 100 in Matrix Multiplication Result:\n", greater_than_100)

matrix1[matrix1 < 10] = 0
matrix2[matrix2 < 10] = 0
print("\nMatrix 1 after replacing <10 with 0:\n", matrix1)
print("\nMatrix 2 after replacing <10 with 0:\n", matrix2)

stacked = np.vstack((matrix1, matrix2))
print("\nVertically Stacked Matrices:\n", stacked)

#Problem 3:

import pandas as pd

sales_data = {
    "OrderID": [101, 102, 103, 104, 105, 106],
    "Customer": ["Ali", "Sara", "Ahmed", "Ali", "Zain", "Sara"],
    "City": ["Karachi", "Lahore", "Karachi", "Islamabad", "Lahore", "Karachi"],
    "Category": ["Electronics", "Clothing", "Electronics", "Groceries", "Clothing", "Electronics"],
    "Amount": [12000, 3500, None, 2400, 5200, 15000]
}

df = pd.DataFrame(sales_data)

print("First 3 rows:")
print(df.head(3))

print("\nMissing Values:")
print(df.isnull().sum())

median_value = df["Amount"].median()
df["Amount"] = df["Amount"].fillna(median_value)

df["Amount"] = df["Amount"].astype(int)

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data:")
print(df)

# Problem 4

df["HighValue"] = df["Amount"] > 10000

print("\nHigh Value Column Added:")
print(df)

karachi_orders = df[df["City"] == "Karachi"]
print("\nOrders from Karachi:")
print(karachi_orders)

electronics_high = df[(df["Category"] == "Electronics") & (df["Amount"] > 10000)]
print("\nElectronics Orders > 10000:")
print(electronics_high)

sorted_df = df.sort_values(by="Amount", ascending=False)
print("\nSorted by Amount:")
print(sorted_df)

top_customers = df.groupby("Customer")["Amount"].sum().sort_values(ascending=False).head(2)
print("\nTop 2 Customers by Spending:")
print(top_customers)

#Problem 5

revenue_city = df.groupby("City")["Amount"].sum()
print("\nTotal Revenue per City:")
print(revenue_city)

avg_category = df.groupby("Category")["Amount"].mean()
print("\nAverage Order Amount per Category:")
print(avg_category)

unique_customers = df.groupby("City")["Customer"].nunique()
print("\nUnique Customers per City:")
print(unique_customers)

pivot_table = pd.pivot_table(
    df,
    values="Amount",
    index="City",
    columns="Category",
    aggfunc="sum"
)

print("\nPivot Table (City vs Category):")
print(pivot_table)

revenue_city_df = revenue_city.reset_index()
print("\nRevenue per City (Reset Index):")
print(revenue_city_df)

# Advanced Challenge 

df["TaxedAmount"] = df["Amount"] * 1.15

df["City"] = df["City"].str.lower()

df = df.sort_values(by="Amount", ascending=False)
df_unique = df.drop_duplicates(subset="Customer", keep="first")

print("\nAfter Removing Duplicate Customers:")
print(df_unique)

summary = {
    "total_orders": len(df),
    "total_revenue": df["Amount"].sum(),
    "average_order": df["Amount"].mean(),
    "top_city": df.groupby("City")["Amount"].sum().idxmax()
}

print("\nSummary Statistics:")
print(summary)

df_unique.to_csv("final_sales_report.csv", index=False)

print("\nFinal processed data saved to final_sales_report.csv")