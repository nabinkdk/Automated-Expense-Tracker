class Expense:
    def __init__(self, date, title, expense):
        self.date = date
        self.title = title
        self.expense = expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Added Successfully !")

    def remove_expense(self, index):
        if index >= 0 and index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed Successfully")
        else:
            print("Invalid expense index.")

    def view_expense(self):
        if len(self.expenses) == 0:
            print("No expenses Found !")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(
                    f"{i}. Date:{expense.date}, Title:{expense.title}, Amount:${expense.expense}"
                )

    def total_expense(self):
        total = sum(amt.expense for amt in self.expenses)
        print(f"Total Expenses: ${total:.2f}")


def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expenses")
        print("2. Remove Expenses")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = int(input("Enter a choice(1-5):\t"))
        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            title = input("Enter a Title: ")
            amt = float(input("Enter the amount: "))
            expense = Expense(date, title, amt)
            tracker.add_expense(expense)
        elif choice == 2:
            index = int(input("Enter a index to remove"))
            tracker.remove_expense(index - 1)

        elif choice == 3:
            tracker.view_expense()
        elif choice == 4:
            tracker.total_expense()
        elif choice == 5:
            print("Exiting .....!")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
