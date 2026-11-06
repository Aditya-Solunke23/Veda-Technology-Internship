from services import services_menu
from programs import programs_menu
from inquiries import inquiries_menu
from requests import requests_menu
from search import search_all_records
from reports import view_business_report


def main():
    while True:
        print("\n================================================")
        print(" VEDA TECHNOLOGY BUSINESS & SERVICE MANAGEMENT")
        print("================================================")
        print("1. Manage Digital Services")
        print("2. Manage Technology, Training & Internship Programs")
        print("3. Manage Customer Inquiries")
        print("4. Manage Service Requests")
        print("5. Search Across All Records")
        print("6. View Business Reports")
        print("7. Exit")
        print("================================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            services_menu()

        elif choice == "2":
            programs_menu()

        elif choice == "3":
            inquiries_menu()

        elif choice == "4":
            requests_menu()

        elif choice == "5":
            search_all_records()

        elif choice == "6":
            view_business_report()

        elif choice == "7":
            print("\nThank you for using Veda Technology Business & Service Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()