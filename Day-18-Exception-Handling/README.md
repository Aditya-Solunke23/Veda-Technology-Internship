
# Day 18 - Exception Handling

## Project Description
A menu-driven Python program demonstrating how to handle common runtime exceptions safely and display meaningful error messages.

## Objective
Practice exception handling using try, except, else, and finally.

## Technology Used
- Python

## Features
- Handles invalid numeric input
- Prevents division-by-zero crashes
- Handles missing dictionary keys
- Handles invalid list indexes
- Handles missing files and file permission errors
- Validates square-root input
- Uses specific exception handlers
- Demonstrates finally blocks

## Exceptions Demonstrated
1. ValueError - invalid numeric input
2. ZeroDivisionError - division by zero
3. KeyError - missing dictionary key
4. IndexError - invalid list index
5. FileNotFoundError - missing file
6. PermissionError - file access denied
7. ValueError - negative square-root input

## Concepts Practiced
- try and except
- else and finally
- Raising exceptions
- Input validation
- Functions
- File handling
- Menu-driven programming

## How to Run
```bash
python exception_handling.py
```

## Interview Questions

### 1. What is exception handling?
Exception handling allows a program to respond to runtime problems without terminating unexpectedly.

### 2. What is the difference between an error and an exception?
An exception is a runtime event that a program can often handle. The term error is broader and can also refer to syntax errors and other problems.

### 3. When should finally be used?
A finally block is used for cleanup or actions that should run whether an operation succeeds or raises an exception.

### 4. Why avoid catching every exception blindly?
Specific exception handlers make failures easier to diagnose and prevent unrelated programming errors from being hidden.
