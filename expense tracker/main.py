class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        # TODO: ask for amount, category, description and append to self.expenses
        pass

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