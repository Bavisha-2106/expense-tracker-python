# Expense Tracker

import json
FILE_NAME = "expenses.json"
expenses = []

def showMenu():
    print("\n1. Add expense")
    print("2. View all expense")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Delete expense")
    print("6. Exit")

def addExpense():
    category = input("Enter your category: ")
    amount = float(input("Enter the total amount: "))
    description = input("Enter a description: ")

    expense = {
        "category" : category,
        "amount" : amount,
        "description" : description
    }

    expenses.append(expense)

    print("Expense added successfully.")

    save_expenses()

def viewExpense():
    if not expenses:
        print("No expenses found.")
        return
    
    for expense in expenses:
        print(f"\nCategory: {expense['category']}\nAmount: {expense['amount']}\nDescription: {expense['description']}")

def totalSpending():
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total amount spent: {total}")

def spendingByCategory():
    if not expenses:
        print("No expenses found.")
        return
    
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nSpending by category:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

def deleteExpense():
    index = int(input("Enter expense number to delete (starting from 1): "))

    if index < 1 or index > len(expenses):
        print("Invalid expense number.")
        return

    expenses.pop(index - 1)
    save_expenses()
    print("Expense deleted successfully.")


def load_expenses():
    global expenses
    try:
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    
def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent = 4)


if __name__ == "__main__":
    load_expenses()

    while True:
        showMenu()

        try:
            option = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Enter a valid input.")
            continue

        if option == 1:
            addExpense()
        elif option == 2:
            viewExpense()
        elif option == 3:
            totalSpending()
        elif option == 4:
            spendingByCategory()
        elif option == 5:
            deleteExpense()
        elif option == 6:
            print("Exiting...")
            break
        else:
            print("Invalid option")
