import json
import os

FILENAME = "expenses.json"

def load_expenses():
    """Loads expense records from the JSON file."""
    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read expenses.json or file is corrupted. Starting with an empty database.")
        return []

def save_expenses(expenses):
    """Saves the expense records to the JSON file."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except IOError:
        print("Error: Failed to write data to file.")

def add_expense(expenses):
    """Adds a new expense record."""
    item = input("Enter expense item name: ").strip()
    if not item:
        print("Error: Item name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Error: Amount must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input for amount. Please enter a valid number.")
        return

    expenses.append({"item": item, "amount": amount})
    save_expenses(expenses)
    print(f"Expense '{item}' of ${amount:.2f} added successfully!")

def view_expenses(expenses):
    """Displays all expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- Expense List ---")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['item']} - ${expense['amount']:.2f}")

def calculate_total(expenses):
    """Calculates and displays the total sum of all expenses."""
    if not expenses:
        print("\nNo expenses to calculate.")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spending: ${total:.2f}")

def delete_expense(expenses):
    """Deletes an expense by item name or list index."""
    if not expenses:
        print("\nNo expenses available to delete.")
        return

    view_expenses(expenses)
    search_term = input("\nEnter the item name or number to delete: ").strip().lower()

    # Try deleting by number index
    if search_term.isdigit():
        idx = int(search_term) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            save_expenses(expenses)
            print(f"Removed '{removed['item']}' (${removed['amount']:.2f}).")
            return

    # Delete by item name match
    for i, expense in enumerate(expenses):
        if expense["item"].lower() == search_term:
            removed = expenses.pop(i)
            save_expenses(expenses)
            print(f"Removed '{removed['item']}' (${removed['amount']:.2f}).")
            return

    print("Expense not found.")

def main():
    """Main application loop."""
    expenses = load_expenses()

    while True:
        print("\n===== JSON EXPENSE MANAGER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Exiting Expense Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()