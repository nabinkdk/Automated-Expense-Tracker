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
    
    def remove_expense(self,index):
        if index>=0 and index<len(self.expenses):
            del self.expenses[index]
            print("Expense removed Successfully")
        else:
            print("Invalid expense index.")
         