import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "inquiries.json"


def load_inquiries():
    """Load inquiries from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_inquiries(inquiries):
    """Save inquiries to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(inquiries, file, indent=4)


def add_inquiry():
    """Add a new customer inquiry."""
    inquiries = load_inquiries()

    customer_name = input("Enter customer name: ").strip()
    email = input("Enter customer email: ").strip()
    subject = input("Enter inquiry subject: ").strip()
    message = input("Enter inquiry message: ").strip()

    if not customer_name or not subject or not message:
        print("Error: Name, subject, and message are required.")
        return

    inquiry = {
        "id": len(inquiries) + 1,
        "customer_name": customer_name,
        "email": email,
        "subject": subject,
        "message": message,
        "status": "Open"
    }

    inquiries.append(inquiry)
    save_inquiries(inquiries)

    print("Inquiry added successfully!")


def view_inquiries():
    """Display all customer inquiries."""
    inquiries = load_inquiries()

    if not inquiries:
        print("No inquiries found.")
        return

    print("\n========== CUSTOMER INQUIRIES ==========")

    for inquiry in inquiries:
        print(f"\nInquiry ID: {inquiry['id']}")
        print(f"Customer: {inquiry['customer_name']}")
        print(f"Email: {inquiry['email']}")
        print(f"Subject: {inquiry['subject']}")
        print(f"Message: {inquiry['message']}")
        print(f"Status: {inquiry['status']}")

    print("\n========================================")


def search_inquiries():
    """Search inquiries by customer name or status."""
    inquiries = load_inquiries()

    search_term = input(
        "Search by customer name or status: "
    ).strip().lower()

    results = [
        inquiry for inquiry in inquiries
        if search_term in inquiry["customer_name"].lower()
        or search_term in inquiry["status"].lower()
    ]

    if not results:
        print("No matching inquiries found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for inquiry in results:
        print(
            f"ID: {inquiry['id']} | "
            f"Customer: {inquiry['customer_name']} | "
            f"Subject: {inquiry['subject']} | "
            f"Status: {inquiry['status']}"
        )


def update_inquiry_status():
    """Update the status of an inquiry."""
    inquiries = load_inquiries()

    try:
        inquiry_id = int(input("Enter inquiry ID: "))
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
        return

    for inquiry in inquiries:
        if inquiry["id"] == inquiry_id:
            print("Available statuses: Open, In Progress, Resolved")

            new_status = input("Enter new status: ").strip().title()

            valid_statuses = ["Open", "In Progress", "Resolved"]

            if new_status not in valid_statuses:
                print("Error: Invalid status.")
                return

            inquiry["status"] = new_status
            save_inquiries(inquiries)

            print("Inquiry status updated successfully!")
            return

    print("Inquiry ID not found.")


def inquiry_menu():
    """Display the inquiry management menu."""
    while True:
        print("\n====== INQUIRY MANAGEMENT ======")
        print("1. Add Inquiry")
        print("2. View All Inquiries")
        print("3. Search Inquiries")
        print("4. Update Inquiry Status")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_inquiry()
        elif choice == "2":
            view_inquiries()
        elif choice == "3":
            search_inquiries()
        elif choice == "4":
            update_inquiry_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    inquiry_menu()