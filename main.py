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
                    f"{i}. Date:{expense.date}, Title:{expense.title}, Amount:{expense.expense}"
                )
    
