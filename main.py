class Expense:
    def __init__(self, date, title, expense):
        self.date = date
        self.title = title
        self.expense = expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        with open("expense.txt", "a") as f:
            f.write(f"{expense.date},{expense.title},{expense.expense}\n")
        print("Added Successfully!")

    def load_expenses(self):
        try:
            with open("expense.txt", "r") as f:
                for line in f:
                    date, title, amt = line.strip().split(",")
                    self.expenses.append(Expense(date, title, float(amt)))
        except FileNotFoundError:
            pass

    def view_expense(self):
        if not self.expenses:
            print("No expenses Found!")
            return

        for i, e in enumerate(self.expenses, start=1):
            print(f"{i}. Date:{e.date}, Title:{e.title}, Amount:${e.expense}")

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_all()
            print("Expense removed Successfully")
        else:
            print("Invalid expense index")

    def save_all(self):
        with open("expense.txt", "w") as f:
            for e in self.expenses:
                f.write(f"{e.date},{e.title},{e.expense}\n")

    def total_expense(self):
        total = sum(e.expense for e in self.expenses)
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

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            title = input("Enter title: ")
            amt = float(input("Enter amount: "))
            tracker.add_expense(Expense(date, title, amt))

        elif choice == "2":
            index = int(input("Enter index to remove: "))
            tracker.remove_expense(index - 1)

        elif choice == "3":
            tracker.view_expense()

        elif choice == "4":
            tracker.total_expense()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__=="__main__":
    main()