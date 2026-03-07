# Lab 05 – NumPy & Pandas

## Difference Between NumPy and Pandas

NumPy is mainly used for numerical computing with arrays and matrices.  
It provides fast mathematical operations and vectorized computations.

Pandas is built on top of NumPy and is used for handling structured data.
It provides DataFrame and Series objects which allow easy data manipulation,
cleaning, grouping, filtering, and analysis.

## Why Vectorization is Preferred Over Loops

Vectorized operations perform calculations on entire arrays or columns at once.
This is faster and more efficient because it uses optimized C-level
implementations instead of Python loops.

Example:
df["TaxedAmount"] = df["Amount"] * 1.15

Instead of looping through each row.

## Handling Missing Data

Missing values in the "Amount" column were identified using `isnull()`.
They were replaced using the median value of the column with `fillna()`.
This prevents loss of data and keeps the dataset balanced.

Example:
df["Amount"] = df["Amount"].fillna(df["Amount"].median())