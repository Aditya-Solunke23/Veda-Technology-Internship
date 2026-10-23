import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Store expenses in a CSV file
DATA_FILE = Path(__file__).parent / "expenses.csv"

FIELDNAMES = ["date", "category", "description", "amount"]


def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_expenses():
    """Load expense records from the CSV file."""
    initialize_file()

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_expense(date, category, description, amount):
    """Save a new expense record."""
    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}"
        })


def get_valid_date():
    """Get a valid date from the user."""
    while True:
        date_input = input(
            "Enter expense date (YYYY-MM-DD), or press Enter for today: "
        ).strip()

        if not date_input:
            return datetime.today().strftime("%Y-%m-%d")

        try:
            return datetime.strptime(
                date_input, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def get_valid_amount():
    """Accept only positive numeric expense amounts."""
    while True:
        try:
            amount = float(input("Enter amount (₹): ").strip())

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


def add_expense():
    """Collect and save an expense."""
    print("\n--- Add New Expense ---")

    date = get_valid_date()

    while True:
        category = input("Enter category (Food, Travel, Bills, etc.): ").strip()
        if category:
            category = category.title()
            break
        print("Category cannot be empty.")

    while True:
        description = input("Enter description: ").strip()
        if description:
            break
        print("Description cannot be empty.")

    amount = get_valid_amount()

    save_expense(date, category, description, amount)

    print("\nExpense added successfully!")
    print(f"Date: {date}")
    print(f"Category: {category}")
    print(f"Description: {description}")
    print(f"Amount: ₹{amount:.2f}")


def view_expenses():
    """Display all saved expenses."""
    expenses = load_expenses()

    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 75)
    print(f"{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':>12}")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<15} "
            f"{expense['description'][:24]:<25} "
            f"₹{float(expense['amount']):>10.2f}"
        )

    print("-" * 75)


def show_summary():
    """Display total and category-wise spending."""
    expenses = load_expenses()

    print("\n--- Spending Summary ---")

    if not expenses:
        print("No expenses available for the summary.")
        return

    category_totals = defaultdict(float)
    total_spending = 0.0

    for expense in expenses:
        amount = float(expense["amount"])
        category_totals[expense["category"]] += amount
        total_spending += amount

    print("\nCategory-wise Spending:")

    for category, total in sorted(category_totals.items()):
        print(f"{category:<20} ₹{total:.2f}")

    print("-" * 35)
    print(f"{'Total Spending':<20} ₹{total_spending:.2f}")
    print(f"Number of Expenses: {len(expenses)}")


def show_monthly_summary():
    """Display expenses for a selected month."""
    expenses = load_expenses()

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Please use YYYY-MM.")
        return

    monthly_expenses = [
        expense for expense in expenses
        if expense["date"].startswith(month)
    ]

    print(f"\n--- Spending Summary for {month} ---")

    if not monthly_expenses:
        print("No expenses found for this month.")
        return

    category_totals = defaultdict(float)
    total = 0.0

    for expense in monthly_expenses:
        amount = float(expense["amount"])
        category_totals[expense["category"]] += amount
        total += amount

    for category, amount in sorted(category_totals.items()):
        print(f"{category:<20} ₹{amount:.2f}")

    print("-" * 35)
    print(f"{'Monthly Total':<20} ₹{total:.2f}")
    print(f"Number of Expenses: {len(monthly_expenses)}")


def main():
    """Display the main menu."""
    initialize_file()

    while True:
        print("\n===================================")
        print("       SIMPLE EXPENSE TRACKER")
        print("===================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Spending Summary")
        print("4. View Monthly Summary")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            show_monthly_summary()
        elif choice == "5":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
