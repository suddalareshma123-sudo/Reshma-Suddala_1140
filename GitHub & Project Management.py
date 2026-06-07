import json
import os
DATA_FILE = "expenses.json"

def load_expenses():
    """Loads expenses from the JSON file. Creates one if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    """Saves the current list of expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Feature 1: Adds a new expense with validation."""
    print("\n--- Add New Expense ---")
    name = input("Enter expense name: ").strip()
    if not name:
        print(" Error: Expense name cannot be empty.")
        return

    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount ($): "))
        if amount <= 0:
            print(" Error: Amount must be greater than 0.")
            return
    except ValueError:
        print(" Error: Invalid amount. Please enter a number.")
        return
    expense_id = max([e["id"] for e in expenses], default=0) + 1

    new_expense = {
        "id": expense_id,
        "name": name,
        "description": description,
        "amount": amount
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print(f" Expense '{name}' added successfully with ID {expense_id}!")

def view_expenses(expenses):
    """Feature 2: Displays all recorded expenses."""
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'ID':<5} | {'Name':<20} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for e in expenses:
        print(f"{e['id']:<5} | {e['name']:<20} | ${e['amount']:<9.2f} | {e['description']}")

def delete_expense(expenses):
    """Feature 3: Deletes an expense by its unique ID."""
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return

    try:
        del_id = int(input("Enter the ID of the expense to delete: "))
    except ValueError:
        print(" Error: Invalid ID format.")
        return

    for expense in expenses:
        if expense["id"] == del_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print(f" Expense ID {del_id} deleted successfully.")
            return

    print(" Error: Expense ID not found.")

def total_spending(expenses):
    """Feature 4: Calculates and displays total spending."""
    print("\n--- Total Spending ---")
    total = sum(e["amount"] for e in expenses)
    print(f" Total Amount Spent: ${total:.2f}")

def main():
    """Main program loop and CLI menu interface."""
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("     EXPENSE TRACKER CLI      ")
        print("==============================")
        print("1.  Add Expense")
        print("2.  View Expenses")
        print("3.  Delete Expense")
        print("4.  Total Spending")
        print("5.  Exit")
        print("==============================")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            total_spending(expenses)
        elif choice == "5":
            print("\nThank you for using Expense Tracker CLI! Bye!")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()