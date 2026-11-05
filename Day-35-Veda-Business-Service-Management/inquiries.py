from models import CustomerInquiry
from storage import load_data, save_data


FILE_NAME = "inquiries.json"


def view_inquiries():
    inquiries = load_data(FILE_NAME)

    if not inquiries:
        print("\nNo customer inquiries found.")
        return

    print("\n========== CUSTOMER INQUIRIES ==========")

    for inquiry in inquiries:
        print(f"ID: {inquiry['inquiry_id']}")
        print(f"Customer: {inquiry['customer_name']}")
        print(f"Email: {inquiry['email']}")
        print(f"Subject: {inquiry['subject']}")
        print(f"Message: {inquiry['message']}")
        print(f"Status: {inquiry['status']}")
        print(f"Date: {inquiry['created_date']}")
        print("----------------------------------------")


def add_inquiry():
    inquiries = load_data(FILE_NAME)

    inquiry_id = f"IN{len(inquiries) + 1:03}"

    customer_name = input("Enter customer name: ").strip()
    email = input("Enter customer email: ").strip()
    subject = input("Enter inquiry subject: ").strip()
    message = input("Enter inquiry message: ").strip()

    if not customer_name or not email or not subject or not message:
        print("All fields are required.")
        return

    if "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        return

    inquiry = CustomerInquiry(
        inquiry_id,
        customer_name,
        email,
        subject,
        message
    )

    inquiries.append(inquiry.to_dict())

    if save_data(FILE_NAME, inquiries):
        print(f"\nInquiry added successfully! ID: {inquiry_id}")


def search_inquiries():
    inquiries = load_data(FILE_NAME)

    keyword = input("Search by customer name, subject, or status: ").strip().lower()

    results = [
        inquiry for inquiry in inquiries
        if keyword in inquiry["customer_name"].lower()
        or keyword in inquiry["subject"].lower()
        or keyword in inquiry["status"].lower()
    ]

    if not results:
        print("No matching inquiries found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for inquiry in results:
        print(
            f"{inquiry['inquiry_id']} | "
            f"{inquiry['customer_name']} | "
            f"{inquiry['subject']} | "
            f"{inquiry['status']}"
        )


def update_inquiry_status():
    inquiries = load_data(FILE_NAME)

    inquiry_id = input("Enter inquiry ID to update: ").strip().upper()

    for inquiry in inquiries:
        if inquiry["inquiry_id"] == inquiry_id:
            print("\nCurrent status:", inquiry["status"])
            print("1. Open")
            print("2. In Progress")
            print("3. Resolved")
            print("4. Closed")

            choice = input("Select new status: ").strip()

            statuses = {
                "1": "Open",
                "2": "In Progress",
                "3": "Resolved",
                "4": "Closed"
            }

            if choice not in statuses:
                print("Invalid status.")
                return

            inquiry["status"] = statuses[choice]

            if save_data(FILE_NAME, inquiries):
                print("Inquiry status updated successfully.")

            return

    print("Inquiry ID not found.")


def inquiries_menu():
    while True:
        print("\n========== CUSTOMER INQUIRY MANAGEMENT ==========")
        print("1. View Inquiries")
        print("2. Add Inquiry")
        print("3. Search Inquiries")
        print("4. Update Inquiry Status")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_inquiries()
        elif choice == "2":
            add_inquiry()
        elif choice == "3":
            search_inquiries()
        elif choice == "4":
            update_inquiry_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")