# Day 10 - Contact Book Using Dictionaries

contacts = {}


def add_contact():
    contact_id = input("Enter contact ID or phone number: ").strip()

    if not contact_id:
        print("Contact ID cannot be empty.")
        return

    if contact_id in contacts:
        print("A contact with this ID already exists.")
        return

    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contacts[contact_id] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\n========== CONTACTS ==========")

    for contact_id, contact in contacts.items():
        print(f"ID    : {contact_id}")
        print(f"Name  : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print("------------------------------")

    print("==============================")


def search_contact():
    contact_id = input("Enter contact ID or phone number to search: ").strip()

    if contact_id in contacts:
        contact = contacts[contact_id]

        print("\n========== CONTACT FOUND ==========")
        print(f"ID    : {contact_id}")
        print(f"Name  : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print("===================================")
    else:
        print("Contact not found.")


def update_contact():
    contact_id = input("Enter contact ID to update: ").strip()

    if contact_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[contact_id]

    print("\nEnter new information:")

    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()

    if name:
        contact["name"] = name

    if phone:
        contact["phone"] = phone

    if email:
        contact["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    contact_id = input("Enter contact ID to delete: ").strip()

    if contact_id in contacts:
        deleted_contact = contacts.pop(contact_id)
        print(
            f"Contact '{deleted_contact['name']}' "
            "deleted successfully."
        )
    else:
        print("Contact not found.")


def display_menu():
    print("\n========================================")
    print("            CONTACT BOOK")
    print("========================================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("========================================")


# Main program
while True:
    display_menu()

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using the Contact Book!")
        print("========================================")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 6.")