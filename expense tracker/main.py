import os
import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def save_expenses(self, filename="expenses.json"):
        # Force Python to save in scripts folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, filename)
        with open(filename, "w") as f:
            json.dump(self.expenses, f, indent=4)
        print(f"Expenses saved to: {full_path}.")

    def load_expenses(self, filename="expenses.json"):
        # Force Python to load file from scripts folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, filename)

        try:
            with open(filename, "r") as f:
                self.expenses = json.load(f)
            print("\nExpenses loaded successfully.")
        except FileNotFoundError:
            print("\nCould not find file 'expenses.json'.")
        except json.JSONDecodeError:
            print("\nExpenses file is corrupted. Starting with empty list.")

    def add_expense(self):
        print("\n----- Add Expense -----")

        # Ask user for amount, make sure valid number
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        # Ask for category and description(optional)
        category = input("Enter category(Food, Transport, Bills, Entertainment, Misc): ").title()
        description = input("Enter short description (optional): ").title()

        # Make expense entry into dict
        expense = {
            "amount": amount,
            "category": category,
            "description": description if description else "No description"
        }

        # Add to list of expenses
        self.expenses.append(expense)

        # Confirmation message
        print(f"Added ${amount:.2f} - {category} ({description})")
        
        # Automatically save after adding expense
        self.save_expenses()

    def view_expenses(self):
        # Check if list is empty
        if not self.expenses:
            print("\nNo expenses added.")
            return
        
        print("\n----- All Expenses -----")
        # Enumerate - adds counter to iterable(expense list) starting at 1
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. ${expense['amount']:.2f} - {expense['category']} ({expense['description']})")
        print("------------------------\n")

    def filter_by_category(self, category):
        return [
            expense for expense in self.expenses
            if expense['category'].lower() == category.lower()
        ]

    def show_filtered(self, filtered, category):
        if not filtered:
            print(f"\nNo expenses found in category '{category}'.")
            return
        
        print(f"\nExpenses in category '{category}'.")
        total = 0
        for i, expense in enumerate(filtered, start=1):
            print(f"{i}. ${expense['amount']:.2f} - {expense['description']}")
            total += expense['amount']

        print(f"\nTotal spent in '{category}: ${total:.2f}")

    def show_total(self):
        # Sum each expense 'amount' and print
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Spent: ${total:.2f}")

    def menu(self):
        print("\n----- Expense Tracker -----\n")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Show Total Spent")
        print("5. Exit")
        choice = input("Enter choice: ")
        return choice
    
def main():
    tracker = ExpenseTracker() # Creates object of the class
    tracker.load_expenses() # Automatically load saved expenses on start

    while True:
        choice = tracker.menu()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            category = input("Enter a category to filter(Food, Transport, Bills, Entertainment, Misc): ")
            filtered = tracker.filter_by_category(category)
            tracker.show_filtered(filtered, category)
        elif choice == "4":
            tracker.show_total()
        elif choice == "5":
            print("\nExiting Program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()