# Day 23 – Simple Expense Tracker

## Overview
The Simple Expense Tracker is a Python-based application that records and manages personal expenses. It stores expense details in a CSV file and generates category-wise, total, and monthly spending summaries.

## Features
- Add expenses with date, category, description, and amount.
- View all recorded expenses.
- Store expense records persistently in a CSV file.
- Generate category-wise spending summaries.
- Calculate total spending.
- Generate monthly expense reports.
- Validate user inputs.

## Technologies Used
- Python
- CSV module
- pathlib
- datetime
- collections

## Concepts Practiced
- Functions and modular programming
- Lists and dictionaries
- File handling
- CSV data processing
- Input validation and exception handling
- Data aggregation and reporting
- Date formatting and monthly filtering

## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

   python expense_tracker.py

4. Select an option from the menu.
5. Add expenses and generate reports.

## Data Storage
Expense records are stored in `expenses.csv`. The data remains available when the program is closed and reopened.

## Future Improvements
- Edit and delete expense records.
- Export monthly reports.
- Display charts showing spending patterns.
- Add expense budgets and budget alerts.
- Build a graphical user interface.