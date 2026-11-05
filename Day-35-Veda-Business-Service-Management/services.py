from models import DigitalService
from storage import load_data, save_data


FILE_NAME = "services.json"


def view_services():
    services = load_data(FILE_NAME)

    if not services:
        print("\nNo digital services found.")
        return

    print("\n========== DIGITAL SERVICES ==========")

    for service in services:
        print(f"ID: {service['service_id']}")
        print(f"Name: {service['name']}")
        print(f"Category: {service['category']}")
        print(f"Description: {service['description']}")
        print(f"Price: ₹{service['price']}")
        print(f"Status: {service['status']}")
        print("-------------------------------------")


def add_service():
    services = load_data(FILE_NAME)

    service_id = f"DS{len(services) + 1:03}"

    name = input("Enter service name: ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        price = float(input("Enter service price: ₹"))

        if price < 0:
            print("Price cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid numeric price.")
        return

    if not name or not category:
        print("Service name and category are required.")
        return

    service = DigitalService(
        service_id,
        name,
        category,
        description,
        price
    )

    services.append(service.to_dict())

    if save_data(FILE_NAME, services):
        print(f"\nService added successfully! ID: {service_id}")


def search_services():
    services = load_data(FILE_NAME)

    keyword = input("Enter service name or category to search: ").strip().lower()

    results = [
        service for service in services
        if keyword in service["name"].lower()
        or keyword in service["category"].lower()
    ]

    if not results:
        print("No matching services found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for service in results:
        print(f"{service['service_id']} | {service['name']} | {service['category']} | ₹{service['price']}")


def services_menu():
    while True:
        print("\n========== DIGITAL SERVICES ==========")
        print("1. View Services")
        print("2. Add Service")
        print("3. Search Services")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_services()
        elif choice == "2":
            add_service()
        elif choice == "3":
            search_services()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")