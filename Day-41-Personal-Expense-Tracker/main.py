from expense_manager import (
    add_expense,
    view_expenses,
    edit_expense,
    delete_expense
)

from search import search_menu
from categories import display_categories


def main():

    while True:

        print("\n" + "=" * 50)
        print("       PERSONAL EXPENSE & BUDGET TRACKER")
        print("=" * 50)

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Search and Filter Expenses")
        print("6. View Expense Categories")
        print("7. Exit")

        print("=" * 50)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            edit_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            search_menu()

        elif choice == "6":
            display_categories()

        elif choice == "7":
            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()