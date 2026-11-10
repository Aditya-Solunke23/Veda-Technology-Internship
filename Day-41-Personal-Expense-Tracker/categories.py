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


def display_categories():
    """Display all available expense categories."""

    print("\n========== EXPENSE CATEGORIES ==========")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    print("========================================")


def get_category_by_choice():
    """Get a valid category selected by the user."""

    display_categories()

    while True:
        try:
            choice = int(input("Select category number: "))

            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]

            print("Invalid choice. Select a number from the list.")

        except ValueError:
            print("Please enter a valid number.")