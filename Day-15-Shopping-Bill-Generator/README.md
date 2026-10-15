
# Day 15 - Shopping Bill Generator

## Project Description
A Python program that accepts product names, quantities, and prices and generates an itemized shopping bill with subtotal, discount, tax, and final amount.

## Objective
To practice lists, dictionaries, loops, functions, calculations, and input validation.

## Technology Used
- Python

## Features
- Accepts multiple products
- Stores product details using dictionaries
- Calculates each item's total
- Calculates subtotal, discount, and tax
- Generates a formatted itemized bill
- Validates quantities, prices, and percentages
- Formats monetary values to two decimal places

## Concepts Practiced
- Lists and dictionaries
- Functions and return statements
- Loops and conditional statements
- Arithmetic operations
- Input validation
- Exception handling
- Formatted strings

## How to Run
```bash
python shopping_bill.py
```

## Calculation Formulas
- Item total = Quantity × Unit price
- Subtotal = Sum of all item totals
- Discount = Subtotal × Discount rate / 100
- Taxable amount = Subtotal − Discount
- Tax = Taxable amount × Tax rate / 100
- Final amount = Taxable amount + Tax

## Interview Questions

### 1. Which data structure is suitable for product records?
A list of dictionaries is suitable. Each dictionary stores a product's name, quantity, and price, while the list stores multiple products.

### 2. Why separate calculations into functions?
Functions improve code reuse, readability, testing, and maintenance.

### 3. How would you handle invalid quantities?
Validate that quantities are positive integers and handle invalid input using conditions and exception handling.
