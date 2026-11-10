from datetime import datetime
from storage import load_expenses
from categories import CATEGORIES, display_categories


def display_results(results):
    """Display matching expense records."""

    if not results:
        print("\nNo matching expenses found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    print(
        f"{'ID':<10} {'Description':<20} "
        f"{'Amount':<12} {'Date':<12} {'Category'}"
    )

    print("-" * 75)

    total = 0

    for expense in results:
        amount = float(expense.get("amount", 0))
        total += amount

        print(
            f"{expense.get('id', 'N/A'):<10} "
            f"{expense.get('description', 'N/A'):<20} "
            f"Rs.{amount:<9.2f} "
            f"{expense.get('date', 'N/A'):<12} "
            f"{expense.get('category', 'N/A')}"
        )

    print("-" * 75)
    print(f"Matching records: {len(results)}")
    print(f"Total amount: Rs.{total:.2f}")


def search_by_description():
    """Search expenses using their descriptions."""

    expenses = load_expenses()

    keyword = input(
        "\nEnter description keyword: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = [
        expense for expense in expenses
        if keyword in expense.get("description", "").lower()
    ]

    display_results(results)


def filter_by_category():
    """Filter expenses by category."""

    expenses = load_expenses()

    display_categories()

    try:
        choice = int(input("Select category number: "))

        if not 1 <= choice <= len(CATEGORIES):
            print("Invalid category selection.")
            return

        selected_category = CATEGORIES[choice - 1]

        results = [
            expense for expense in expenses
            if expense.get("category") == selected_category
        ]

        print(f"\nExpenses in category: {selected_category}")
        display_results(results)

    except ValueError:
        print("Please enter a valid category number.")


def filter_by_date():
    """Filter expenses for a particular date."""

    expenses = load_expenses()

    date_input = input(
        "\nEnter date (YYYY-MM-DD): "
    ).strip()

    try:
        datetime.strptime(date_input, "%Y-%m-%d")

        results = [
            expense for expense in expenses
            if expense.get("date") == date_input
        ]

        display_results(results)

    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")


def filter_by_amount():
    """Filter expenses within an amount range."""

    expenses = load_expenses()

    try:
        minimum = float(input("Enter minimum amount: Rs."))
        maximum = float(input("Enter maximum amount: Rs."))

        if minimum < 0 or maximum < 0:
            print("Amounts cannot be negative.")
            return

        if minimum > maximum:
            print("Minimum amount cannot exceed maximum amount.")
            return

        results = [
            expense for expense in expenses
            if minimum <= float(expense.get("amount", 0)) <= maximum
        ]

        display_results(results)

    except ValueError:
        print("Please enter valid numeric amounts.")


def advanced_filter():
    """Combine multiple optional filters."""

    expenses = load_expenses()

    print("\n========== ADVANCED FILTER ==========")
    print("Leave a field blank to skip that filter.")

    keyword = input("Description keyword: ").strip().lower()
    category = input("Category name: ").strip().lower()
    date_input = input("Date (YYYY-MM-DD): ").strip()
    minimum_input = input("Minimum amount: ").strip()
    maximum_input = input("Maximum amount: ").strip()

    if date_input:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

    if category and category not in [c.lower() for c in CATEGORIES]:
        print("Invalid category.")
        return

    if bool(minimum_input) != bool(maximum_input):
        print("Enter both minimum and maximum amounts.")
        return

    minimum = None
    maximum = None

    if minimum_input:
        try:
            minimum = float(minimum_input)
            maximum = float(maximum_input)

            if minimum < 0 or maximum < 0 or minimum > maximum:
                print("Invalid amount range.")
                return

        except ValueError:
            print("Amounts must be numeric.")
            return

    results = expenses

    if keyword:
        results = [
            e for e in results
            if keyword in e.get("description", "").lower()
        ]

    if category:
        results = [
            e for e in results
            if e.get("category", "").lower() == category
        ]

    if date_input:
        results = [
            e for e in results
            if e.get("date") == date_input
        ]

    if minimum is not None:
        results = [
            e for e in results
            if minimum <= float(e.get("amount", 0)) <= maximum
        ]

    display_results(results)


def search_menu():
    """Display the search and filtering menu."""

    while True:

        print("\n========== SEARCH & FILTER ==========")
        print("1. Search by Description")
        print("2. Filter by Category")
        print("3. Filter by Date")
        print("4. Filter by Amount Range")
        print("5. Advanced Filter (Combine Filters)")
        print("6. Back to Main Menu")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            search_by_description()

        elif choice == "2":
            filter_by_category()

        elif choice == "3":
            filter_by_date()

        elif choice == "4":
            filter_by_amount()

        elif choice == "5":
            advanced_filter()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Select between 1 and 6.")