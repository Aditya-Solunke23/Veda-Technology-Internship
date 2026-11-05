from models import ServiceRequest
from storage import load_data, save_data


FILE_NAME = "requests.json"


def view_requests():
    requests = load_data(FILE_NAME)

    if not requests:
        print("\nNo service requests found.")
        return

    print("\n========== SERVICE REQUESTS ==========")

    for request in requests:
        print(f"ID: {request['request_id']}")
        print(f"Customer: {request['customer_name']}")
        print(f"Service: {request['service_name']}")
        print(f"Description: {request['description']}")
        print(f"Priority: {request['priority']}")
        print(f"Status: {request['status']}")
        print(f"Date: {request['created_date']}")
        print("-------------------------------------")


def add_request():
    requests = load_data(FILE_NAME)

    request_id = f"SR{len(requests) + 1:03}"

    customer_name = input("Enter customer name: ").strip()
    service_name = input("Enter requested service: ").strip()
    description = input("Enter request description: ").strip()

    print("\nPriority Levels:")
    print("1. Low")
    print("2. Normal")
    print("3. High")
    print("4. Urgent")

    priority_choice = input("Select priority: ").strip()

    priorities = {
        "1": "Low",
        "2": "Normal",
        "3": "High",
        "4": "Urgent"
    }

    if priority_choice not in priorities:
        print("Invalid priority.")
        return

    priority = priorities[priority_choice]

    if not customer_name or not service_name or not description:
        print("All fields are required.")
        return

    request = ServiceRequest(
        request_id,
        customer_name,
        service_name,
        description,
        priority
    )

    requests.append(request.to_dict())

    if save_data(FILE_NAME, requests):
        print(f"\nService request added successfully! ID: {request_id}")


def search_requests():
    requests = load_data(FILE_NAME)

    keyword = input(
        "Search by customer, service, priority, or status: "
    ).strip().lower()

    results = [
        request for request in requests
        if keyword in request["customer_name"].lower()
        or keyword in request["service_name"].lower()
        or keyword in request["priority"].lower()
        or keyword in request["status"].lower()
    ]

    if not results:
        print("No matching service requests found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for request in results:
        print(
            f"{request['request_id']} | "
            f"{request['customer_name']} | "
            f"{request['service_name']} | "
            f"{request['priority']} | "
            f"{request['status']}"
        )


def update_request_status():
    requests = load_data(FILE_NAME)

    request_id = input("Enter request ID to update: ").strip().upper()

    for request in requests:
        if request["request_id"] == request_id:
            print("\nCurrent status:", request["status"])
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")
            print("4. Cancelled")

            choice = input("Select new status: ").strip()

            statuses = {
                "1": "Pending",
                "2": "In Progress",
                "3": "Completed",
                "4": "Cancelled"
            }

            if choice not in statuses:
                print("Invalid status.")
                return

            request["status"] = statuses[choice]

            if save_data(FILE_NAME, requests):
                print("Service request status updated successfully.")

            return

    print("Request ID not found.")


def requests_menu():
    while True:
        print("\n========== SERVICE REQUEST MANAGEMENT ==========")
        print("1. View Service Requests")
        print("2. Add Service Request")
        print("3. Search Service Requests")
        print("4. Update Request Status")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_requests()
        elif choice == "2":
            add_request()
        elif choice == "3":
            search_requests()
        elif choice == "4":
            update_request_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")