
print("========================================")
print("       EXCEPTION HANDLING DEMO")
print("========================================")


def handle_invalid_number():
    print("\n1. INVALID NUMERIC INPUT")
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
    else:
        print(f"You entered: {number}")
    finally:
        print("Numeric input check completed.")


def handle_division():
    print("\n2. DIVISION BY ZERO")
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result:.2f}")
    finally:
        print("Division operation completed.")


def handle_missing_dictionary_key():
    print("\n3. MISSING DICTIONARY KEY")
    student = {"name": "Aditya", "course": "Python"}

    try:
        key = input("Enter a key to access (name/course/age): ").strip()
        value = student[key]
    except KeyError:
        print("Error: The requested key does not exist.")
    else:
        print(f"Value: {value}")
    finally:
        print("Dictionary access completed.")


def handle_invalid_list_index():
    print("\n4. INVALID LIST INDEX")
    numbers = [10, 20, 30]

    try:
        index = int(input("Enter a list index (0-2): "))
        print(f"Value: {numbers[index]}")
    except ValueError:
        print("Error: Index must be an integer.")
    except IndexError:
        print("Error: Index is outside the list range.")
    finally:
        print("List access completed.")


def handle_missing_file():
    print("\n5. MISSING FILE")
    filename = input("Enter a filename to read: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found. Check the filename.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    else:
        print("File content:")
        print(content if content else "(The file is empty.)")
    finally:
        print("File operation completed.")


def handle_negative_square_root():
    print("\n6. INVALID SQUARE ROOT")
    try:
        number = float(input("Enter a non-negative number: "))

        if number < 0:
            raise ValueError("A real square root requires a non-negative number.")

        result = number ** 0.5
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Square root: {result:.2f}")
    finally:
        print("Square root operation completed.")


while True:
    print("\n========== MENU ==========")
    print("1. Invalid numeric input")
    print("2. Division by zero")
    print("3. Missing dictionary key")
    print("4. Invalid list index")
    print("5. Missing file")
    print("6. Invalid square root")
    print("7. Exit")
    print("==========================")

    choice = input("Choose a case (1-7): ").strip()

    if choice == "1":
        handle_invalid_number()
    elif choice == "2":
        handle_division()
    elif choice == "3":
        handle_missing_dictionary_key()
    elif choice == "4":
        handle_invalid_list_index()
    elif choice == "5":
        handle_missing_file()
    elif choice == "6":
        handle_negative_square_root()
    elif choice == "7":
        print("Thank you for exploring exception handling!")
        break
    else:
        print("Error: Choose a valid menu option from 1 to 7.")
