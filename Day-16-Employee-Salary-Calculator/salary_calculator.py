
print("==============================================")
print("          EMPLOYEE SALARY CALCULATOR")
print("==============================================")


# Configurable salary rules (percentages)
SALARY_RULES = {
    "hra_rate": 20.0,
    "da_rate": 10.0,
    "pf_rate": 12.0,
    "tax_rate": 5.0
}


def calculate_salary(basic_salary, rules):
    hra = basic_salary * rules["hra_rate"] / 100
    da = basic_salary * rules["da_rate"] / 100
    gross_salary = basic_salary + hra + da

    pf = basic_salary * rules["pf_rate"] / 100
    tax = gross_salary * rules["tax_rate"] / 100
    total_deductions = pf + tax
    net_salary = gross_salary - total_deductions

    return {
        "basic_salary": basic_salary,
        "hra": hra,
        "da": da,
        "gross_salary": gross_salary,
        "pf": pf,
        "tax": tax,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }


def display_salary(employee, salary):
    print("\n" + "=" * 46)
    print("             SALARY BREAKDOWN")
    print("=" * 46)
    print(f"Employee Name     : {employee['name']}")
    print(f"Employee ID       : {employee['id']}")
    print("-" * 46)
    print(f"Basic Salary      : Rs. {salary['basic_salary']:,.2f}")
    print(f"HRA               : Rs. {salary['hra']:,.2f}")
    print(f"DA                : Rs. {salary['da']:,.2f}")
    print("-" * 46)
    print(f"Gross Salary      : Rs. {salary['gross_salary']:,.2f}")
    print(f"Provident Fund    : Rs. {salary['pf']:,.2f}")
    print(f"Tax               : Rs. {salary['tax']:,.2f}")
    print(f"Total Deductions  : Rs. {salary['total_deductions']:,.2f}")
    print("=" * 46)
    print(f"NET SALARY        : Rs. {salary['net_salary']:,.2f}")
    print("=" * 46)


try:
    employee = {
        "id": input("\nEnter employee ID: ").strip(),
        "name": input("Enter employee name: ").strip()
    }

    if not employee["id"] or not employee["name"]:
        raise ValueError("Employee ID and name cannot be empty.")

    basic_salary = float(input("Enter basic monthly salary (Rs.): "))

    if basic_salary < 0:
        raise ValueError("Salary cannot be negative.")

    salary = calculate_salary(basic_salary, SALARY_RULES)
    display_salary(employee, salary)

except ValueError as error:
    print(f"\nError: {error}")
