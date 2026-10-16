
# Day 16 - Employee Salary Calculator

## Project Description
A Python program that calculates employee gross salary, deductions, and net salary using configurable salary rules.

## Objective
Practice dictionaries, functions, conditions, numeric input validation, and business-rule implementation.

## Technology Used
- Python

## Features
- Accepts employee ID, name, and basic salary
- Calculates HRA and DA allowances
- Calculates provident fund and tax deductions
- Computes gross and net salary
- Stores employee and salary details using dictionaries
- Keeps salary percentages configurable
- Validates employee details and numeric input
- Displays a formatted salary breakdown

## Concepts Practiced
- Dictionaries
- Functions and return values
- Conditional statements
- Arithmetic operations
- Input validation
- Exception handling
- Formatted output

## Salary Formulas
- HRA = Basic Salary × HRA Rate / 100
- DA = Basic Salary × DA Rate / 100
- Gross Salary = Basic Salary + HRA + DA
- PF = Basic Salary × PF Rate / 100
- Tax = Gross Salary × Tax Rate / 100
- Net Salary = Gross Salary − PF − Tax

The percentages used are illustrative practice values and can be modified in `SALARY_RULES`.

## How to Run
```bash
python salary_calculator.py
```

## Interview Questions

### 1. How would you represent employee data?
A dictionary is suitable for storing related information using keys such as employee ID, name, and salary.

### 2. Why separate business rules from input handling?
It makes the program easier to maintain, test, reuse, and update when requirements change.

### 3. How would you modify the program if salary rules changed?
Update the values in `SALARY_RULES`. The calculation functions use these values automatically.
