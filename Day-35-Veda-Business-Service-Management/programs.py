from services import services_menu
from programs import programs_menu


def main():
    while True:
        print("\n===== VEDA TECHNOLOGY SYSTEM =====")
        print("1. Manage Digital Services")
        print("2. Manage Programs")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            services_menu()
        elif choice == "2":
            programs_menu()
        elif choice == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()