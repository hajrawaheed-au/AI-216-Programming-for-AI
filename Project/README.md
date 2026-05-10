# 💰 Expense Tracker System

A simple and user-friendly Expense Tracker project developed using Python, Pandas, and NumPy.

This application helps users manage and analyze their daily expenses. All expense records are permanently stored in a CSV file.

---

# 📌 Features

- Add New Expenses
- View All Expenses
- Search Expenses
- Delete Expenses
- Category-wise Expense Summary
- Highest & Lowest Expense Detection
- Spending Statistics
- CSV File Storage
- Data Analysis using NumPy

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main Programming Language |
| Pandas | Data Handling & CSV Management |
| NumPy | Statistical Calculations |
| CSV File | Data Storage |

---

# 📂 Project Structure

```bash
ExpenseTracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

---

# ▶ How to Run the Project

## Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

---

## Step 2: Install Required Libraries

Open terminal in VS Code and run:

```bash
pip install pandas numpy
```

---


# 📋 Menu Options

| Option | Function |
|--------|----------|
| 1 | Add Expense |
| 2 | View Expenses |
| 3 | Total Spending & Statistics |
| 4 | Category Summary |
| 5 | Search Expense |
| 6 | Highest & Lowest Expense |
| 7 | Delete Expense |
| 0 | Exit Program |

---

# 📊 Statistics Included

The system calculates:

- Total Spending
- Average Spending
- Highest Expense
- Lowest Expense
- Total Entries

using NumPy functions such as:

```python
np.sum()
np.mean()
np.max()
np.min()
```

---

# 📁 CSV File Storage

All expense data is automatically saved inside:

```bash
expenses.csv
```

This allows the data to remain محفوظ even after closing the program.

---

# 🔍 Search Feature

Users can search expenses using:

- Category names
- Description keywords

Examples:

- Food
- Shopping
- Uber
- Burger

---

# 📈 Category Summary

The project groups expenses category-wise and displays total spending for each category.

Example:

```text
Food           PKR 5000
Transport      PKR 2000
Shopping       PKR 7000
```

---

# 🎯 Concepts Used in This Project

This project demonstrates:

- File Handling
- Pandas DataFrames
- NumPy Calculations
- Loops
- Conditional Statements
- Exception Handling
- Searching & Filtering
- GroupBy Operations

---

# 👨‍💻 Author

Developed as a Python Mini Project for learning expense management and data analysis.

---

# 🚀 Future Improvements

Possible future upgrades:

- Monthly Budget System
- Graph Visualization
- Date & Time Tracking
- GUI Interface
- Export Reports
- User Authentication System

---