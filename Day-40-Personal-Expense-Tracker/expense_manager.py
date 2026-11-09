from datetime import datetime
from storage import load_expenses, save_expenses


# Available expense categories
CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Entertainment",
    "Bills",
    "Health",
    "Other"
]


def get_valid_amount():
    """Accept only positive numeric amounts."""

    while True:
        try:
            amount = float(input("Enter expense amount (Rs.): "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_valid_date():
    """Validate expense date in YYYY-MM-DD format."""

    while True:
        expense_date = input(
            "Enter expense date (YYYY-MM-DD): "
        ).strip()

        try:
            datetime.strptime(expense_date, "%Y-%m-%d")
            return expense_date

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def get_valid_category():
    """Display and validate expense categories."""

    print("\nAvailable Categories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Select category number: "))

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            print("Please select a valid category.")

        except ValueError:
            print("Please enter a valid number.")


def generate_expense_id(expenses):
    """Generate a unique expense ID."""

    highest_number = 0

    for expense in expenses:
        expense_id = expense.get("id", "")

        if expense_id.startswith("EXP"):
            try:
                number = int(expense_id[3:])
                highest_number = max(highest_number, number)
            except ValueError:
                continue

    return f"EXP{highest_number + 1:03d}"


def add_expense():
    """Add a new expense."""

    expenses = load_expenses()

    print("\n========== ADD EXPENSE ==========")

    description = input("Enter expense description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    amount = get_valid_amount()
    expense_date = get_valid_date()
    category = get_valid_category()

    expense = {
        "id": generate_expense_id(expenses),
        "description": description,
        "amount": amount,
        "date": expense_date,
        "category": category
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("\nExpense added successfully!")
        print(f"Expense ID: {expense['id']}")


def view_expenses():
    """Display all recorded expenses."""

    expenses = load_expenses()

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'ID':<10} {'Description':<20} "
        f"{'Amount':<12} {'Date':<12} {'Category'}"
    )

    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense.get('id', 'N/A'):<10} "
            f"{expense.get('description', 'N/A'):<20} "
            f"Rs.{expense.get('amount', 0):<9.2f} "
            f"{expense.get('date', 'N/A'):<12} "
            f"{expense.get('category', 'N/A')}"
        )


def edit_expense():
    """Edit an existing expense."""

    expenses = load_expenses()

    print("\n========== EDIT EXPENSE ==========")

    if not expenses:
        print("No expenses available to edit.")
        return

    view_expenses()

    expense_id = input(
        "\nEnter the expense ID to edit: "
    ).strip().upper()

    expense = next(
        (item for item in expenses if item.get("id") == expense_id),
        None
    )

    if expense is None:
        print("Expense ID not found.")
        return

    print("\nLeave a field blank to keep its existing value.")

    new_description = input(
        f"New description [{expense['description']}]: "
    ).strip()

    if new_description:
        expense["description"] = new_description

    while True:
        new_amount = input(
            f"New amount [{expense['amount']}]: "
        ).strip()

        if not new_amount:
            break

        try:
            amount = float(new_amount)

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            expense["amount"] = round(amount, 2)
            break

        except ValueError:
            print("Please enter a valid numeric amount.")

    while True:
        new_date = input(
            f"New date [{expense['date']}] (YYYY-MM-DD): "
        ).strip()

        if not new_date:
            break

        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            expense["date"] = new_date
            break

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")

    print("\nSelect a new category or press Enter to keep the current one.")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        new_category = input(
            f"New category [{expense['category']}]: "
        ).strip()

        if not new_category:
            break

        try:
            choice = int(new_category)

            if 1 <= choice <= len(CATEGORIES):
                expense["category"] = CATEGORIES[choice - 1]
                break

            print("Select a valid category number.")

        except ValueError:
            print("Please enter a valid number.")

    if save_expenses(expenses):
        print("\nExpense updated successfully!")


def delete_expense():
    """Delete an existing expense."""

    expenses = load_expenses()

    print("\n========== DELETE EXPENSE ==========")

    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses()

    expense_id = input(
        "\nEnter the expense ID to delete: "
    ).strip().upper()

    expense = next(
        (item for item in expenses if item.get("id") == expense_id),
        None
    )

    if expense is None:
        print("Expense ID not found.")
        return

    confirmation = input(
        f"Are you sure you want to delete {expense_id}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        expenses.remove(expense)

        if save_expenses(expenses):
            print("Expense deleted successfully!")

    else:
        print("Deletion cancelled.")