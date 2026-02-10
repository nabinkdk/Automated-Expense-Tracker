class Expense:
    def __init__(self, date, title, expense):
        self.date = date
        self.title = title
        self.expense = expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    