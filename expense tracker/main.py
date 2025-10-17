class ExpenseTracker:
    def __init__(self):
        self.expenses = []

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
        category = input("Enter category(Food, Transport, Bills, Entertainment, Misc): ")
        description = input("Enter short description (optional): ")

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

    def view_expenses(self):
        # TODO: print all expenses
        pass

    def filter_by_category(self):
        # TODO: filter expenses by category
        pass

    def show_total(self):
        # TODO: sum all amounts and print total
        pass

    def menu(self):
        print("\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Show Total Spent")
        print("5. Exit")
        choice = input("Enter choice: ")
        return choice
    
def main():
    tracker = ExpenseTracker() # Creates object of the class

    while True:
        choice = tracker.menu()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.filter_by_category()
        elif choice == "4":
            tracker.show_total()
        elif choice == "5":
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()