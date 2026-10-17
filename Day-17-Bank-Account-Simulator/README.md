
# Day 17 - Bank Account Simulator

## Project Description
A menu-driven Python application that simulates basic bank account operations, including balance inquiry, deposits, withdrawals, and transaction history.

## Objective
Practice functions, loops, input validation, and state management.

## Technology Used
- Python

## Features
- Check current account balance
- Deposit money
- Withdraw money
- Prevent withdrawals exceeding available balance
- View transaction history
- Validate invalid amounts and menu choices
- Track the balance after each successful transaction

## Concepts Practiced
- Functions
- Global state
- Lists and dictionaries
- Loops and conditional statements
- Input validation
- Exception handling
- State management

## How to Run
```bash
python bank_account.py
```

## Data Structures
- A numeric variable stores the current balance.
- A list stores transaction records.
- Each transaction is represented by a dictionary containing its type, amount, and resulting balance.

## Interview Questions

### 1. How would you maintain application state?
The current balance and transaction list maintain the application's state while it runs.

### 2. Why should invalid withdrawals be rejected?
Rejecting invalid withdrawals prevents negative balances and protects the consistency of account records.

### 3. What data structure is suitable for transaction history?
A list of dictionaries is suitable because it preserves transaction order and allows each transaction to store multiple related fields.
