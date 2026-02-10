# Automated Expense Tracker

A simple command-line application to track and manage personal expenses efficiently. This tool allows you to add, view, remove, and calculate total expenses with ease.

## Features

- **Add Expenses**: Record new expenses with date, title, and amount
- **View Expenses**: Display all recorded expenses in a formatted list
- **Remove Expenses**: Delete specific expenses by index
- **Calculate Total**: Get the sum of all expenses
- **Persistent Storage**: Expenses are automatically saved to `expense.txt`
- **Load on Startup**: Previously saved expenses are loaded when the application starts

## Project Structure

### main.py

The main Python script containing the core functionality of the expense tracker:

#### Classes

**Expense Class**

- Represents a single expense entry
- Attributes:
  - `date`: Date of expense (format: YYYY-MM-DD)
  - `title`: Description/title of the expense
  - `expense`: Amount spent

**ExpenseTracker Class**

- Manages all expense-related operations
- Methods:
  - `add_expense(expense)`: Add a new expense and save to file
  - `load_expenses()`: Load all saved expenses from `expense.txt`
  - `view_expense()`: Display all expenses in a numbered list
  - `remove_expense(index)`: Delete an expense by its index
  - `save_all()`: Save all expenses to `expense.txt`
  - `total_expense()`: Calculate and display the sum of all expenses

#### Main Menu

The application provides an interactive menu with the following options:

1. **Add Expenses** - Enter date, title, and amount
2. **Remove Expenses** - Remove an expense by index number
3. **View Expenses** - Display all recorded expenses
4. **Total Expenses** - Show the total sum of all expenses
5. **Exit** - Close the application

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Select an option from the menu (1-5)

3. Follow the prompts to add, view, or manage expenses

### Example

```
Expense Tracker Menu:
1. Add Expenses
2. Remove Expenses
3. View Expenses
4. Total Expenses
5. Exit

Enter choice (1-5): 1
Enter date (YYYY-MM-DD): 2026-02-10
Enter title: Grocery Shopping
Enter amount: 45.50
Added Successfully!
```

## File Storage

- **expense.txt**: Stores all expenses in CSV format (date, title, amount)
- Format: `YYYY-MM-DD,Item Description,Amount`

## Requirements

- Python 3.x
- No external dependencies required

## Getting Started

1. Clone or download this repository
2. Navigate to the project directory
3. Run `python main.py`
4. Start tracking your expenses!

## Notes

- Dates should be in YYYY-MM-DD format
- Amounts can be decimal values (e.g., 19.99)
- Expenses are persisted across sessions in `expense.txt`
