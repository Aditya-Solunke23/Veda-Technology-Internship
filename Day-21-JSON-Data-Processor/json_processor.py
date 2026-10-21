
import json

print("========================================")
print("          JSON DATA PROCESSOR")
print("========================================")


def load_data(filename):
    """Load employee data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict) or not isinstance(data.get("employees"), list):
        raise ValueError("JSON must contain an 'employees' list.")

    for employee in data["employees"]:
        if not isinstance(employee, dict):
            raise ValueError("Each employee record must be a JSON object.")

        required_keys = {"id", "name", "department", "salary", "skills"}
        if not required_keys.issubset(employee):
            raise ValueError("An employee record is missing required fields.")

    return data["employees"]


def search_employee(employees, name):
    return [
        employee for employee in employees
        if name.lower() in employee["name"].lower()
    ]


def filter_by_department(employees, department):
    return [
        employee for employee in employees
        if employee["department"].lower() == department.lower()
    ]


def summarize_salaries(employees):
    if not employees:
        return 0, 0, 0

    salaries = [employee["salary"] for employee in employees]
    return min(salaries), max(salaries), sum(salaries) / len(salaries)


def save_results(filename, employees):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump({"employees": employees}, file, indent=4)


try:
    employees = load_data("data.json")
    print(f"\nLoaded {len(employees)} employee records successfully.")

    while True:
        print("\n========== MENU ==========")
        print("1. View all employees")
        print("2. Search employee by name")
        print("3. Filter by department")
        print("4. Salary summary")
        print("5. Save IT department records")
        print("6. Exit")
        print("==========================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n========== EMPLOYEES ==========")
            for employee in employees:
                print(
                    f"ID: {employee['id']} | "
                    f"Name: {employee['name']} | "
                    f"Department: {employee['department']} | "
                    f"Salary: Rs. {employee['salary']}"
                )

        elif choice == "2":
            name = input("Enter a name to search: ").strip()
            results = search_employee(employees, name)

            if results:
                for employee in results:
                    print(employee)
            else:
                print("No matching employee found.")

        elif choice == "3":
            department = input("Enter department: ").strip()
            results = filter_by_department(employees, department)

            if results:
                for employee in results:
                    print(employee)
            else:
                print("No employees found in that department.")

        elif choice == "4":
            minimum, maximum, average = summarize_salaries(employees)
            if employees:
                print(f"Lowest salary  : Rs. {minimum:,.2f}")
                print(f"Highest salary : Rs. {maximum:,.2f}")
                print(f"Average salary : Rs. {average:,.2f}")
            else:
                print("No employee records available.")

        elif choice == "5":
            it_employees = filter_by_department(employees, "IT")
            save_results("filtered_employees.json", it_employees)
            print(
                f"Saved {len(it_employees)} IT employee records "
                "to filtered_employees.json."
            )

        elif choice == "6":
            print("Thank you for using the JSON Data Processor!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

except FileNotFoundError:
    print("Error: data.json was not found. Check the project folder.")

except json.JSONDecodeError:
    print("Error: data.json contains invalid JSON.")

except (ValueError, TypeError) as error:
    print(f"Error: Invalid employee data. {error}")

except OSError as error:
    print(f"File operation failed: {error}")
