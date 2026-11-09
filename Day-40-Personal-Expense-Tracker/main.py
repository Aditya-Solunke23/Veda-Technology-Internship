from expense_manager import (
    add_expense,
    view_expenses,
    edit_expense,
    delete_expense
)


def main():

    while True:

        print("\n" + "=" * 45)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 45)

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            edit_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()