import pandas as pd
import numpy as np
import os

FILE = "expenses.csv"

# Load File
if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["Category", "Amount", "Description"])

# Menu
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending & Stats")
    print("4. Category Summary")
    print("5. Search Expense")
    print("6. Highest & Lowest Expense")
    print("7. Delete Expense")
    print("0. Exit")

    choice = input("Enter choice: ")

    # Add Expense
    if choice == "1":

        category = input("Category (Food/Transport/Shopping/Health/Other): ")
        amount = float(input("Amount: "))
        desc = input("Description: ")

        new = pd.DataFrame([[category, amount, desc]],
                           columns=["Category", "Amount", "Description"])

        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(FILE, index=False)

        print("Expense Added!")

    # View Expenses
    elif choice == "2":

        if df.empty:
            print("No Expenses Found!")
        else:
            print("\n", df)

    # Total Spending + Stats
    elif choice == "3":

        if df.empty:
            print("No Data!")
        else:
            amounts = df["Amount"].values

            print("\nTotal Spending  :", np.sum(amounts))
            print("Average Spending:", round(np.mean(amounts), 2))
            print("Highest Expense :", np.max(amounts))
            print("Lowest Expense  :", np.min(amounts))
            print("Total Entries   :", len(df))

    # Category Summary
    elif choice == "4":

        if df.empty:
            print("No Data!")
        else:
            summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

            print("\n--- Spending by Category ---")
            for cat, total in summary.items():
                bar = "█" * int(total // 100)
                print(f"{cat:<15} PKR {total:<8.0f} {bar}")

    # Search Expense
    elif choice == "5":

        keyword = input("Enter keyword to search: ").lower()
        result = df[df["Description"].str.lower().str.contains(keyword) |
                    df["Category"].str.lower().str.contains(keyword)]

        if result.empty:
            print("No match found!")
        else:
            print("\n", result)

    # Highest & Lowest Expense
    elif choice == "6":

        if df.empty:
            print("No Data!")
        else:
            print("\nHighest Expense:")
            print(df.loc[df["Amount"].idxmax()])

            print("\nLowest Expense:")
            print(df.loc[df["Amount"].idxmin()])

    # Delete Expense
    elif choice == "7":

        if df.empty:
            print("No Data!")
        else:
            print(df)
            try:
                row = int(input("Enter row number to delete: "))
                df = df.drop(row).reset_index(drop=True)
                df.to_csv(FILE, index=False)
                print("Deleted Successfully!")
            except:
                print("Invalid Input!")

    # Exit
    elif choice == "0":
        print("Good Bye!")
        break

    else:
        print("Wrong Choice!")