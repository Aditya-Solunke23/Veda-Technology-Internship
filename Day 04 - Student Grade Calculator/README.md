# Day 4 - Student Grade Calculator

## Project Description

This project is a Python-based Student Grade Calculator that accepts marks for multiple subjects, calculates the total marks and percentage, and assigns a grade based on predefined percentage criteria.

The program also validates the marks entered by the user and ensures that each mark is within the allowed range of 0 to 100.

## Objective

The objective of this task is to practice:

- Conditional statements
- Arithmetic operations
- User input
- Type conversion
- Input validation
- Loops
- Basic program logic

## Features

- Accepts marks for multiple subjects
- Validates marks between 0 and 100
- Calculates total marks
- Calculates percentage
- Assigns grades automatically
- Handles invalid input
- Displays results in a clear format

## Grade Criteria

| Percentage | Grade |
|---|---|
| 90% - 100% | A+ |
| 80% - 89% | A |
| 70% - 79% | B |
| 60% - 69% | C |
| 50% - 59% | D |
| 40% - 49% | E |
| Below 40% | F |

## How It Works

1. The user enters the number of subjects.
2. The program accepts marks for each subject.
3. Each mark is validated to ensure it is between 0 and 100.
4. The program calculates the total marks.
5. The percentage is calculated using:

```text
Percentage = (Total Marks / Maximum Marks) × 100

6. The percentage is compared with the predefined grade boundaries.
7. The final total marks, percentage, and grade are displayed.