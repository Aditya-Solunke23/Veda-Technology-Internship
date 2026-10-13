# Day 13 - Prime Number Analyzer

## 📌 Project Description

A Python program that checks whether a number is prime and generates all prime numbers within a specified range.

## 🎯 Objective

The objective of this task is to practice loops, conditions, functions, and basic algorithmic thinking.

## 🛠️ Technology Used

- Python

## ✨ Features

- Checks whether an individual number is prime
- Generates prime numbers within a specified range
- Uses a reusable `is_prime()` function
- Handles numbers such as 0 and 1 correctly
- Handles invalid input
- Uses an optimized prime-checking approach
- Displays results in a formatted manner

## 🧠 Concepts Practiced

- Functions
- `if-elif-else`
- `while` loops
- `for` loops
- Lists
- Modulus operator `%`
- Functions and return values
- Input validation
- Algorithm optimization

## ⚙️ Algorithm

The program determines whether a number is prime using the following steps:

1. If the number is less than 2, it is not prime.
2. If the number is 2, it is prime.
3. If the number is even and greater than 2, it is not prime.
4. Check only odd divisors starting from 3.
5. Continue checking while `divisor * divisor <= number`.
6. If a divisor divides the number exactly, the number is not prime.
7. If no divisor is found, the number is prime.

## ▶️ How to Run

Run the following command:

```bash
python prime_analyzer.py