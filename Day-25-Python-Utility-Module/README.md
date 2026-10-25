# Day 25 – Python Utility Module

## Overview
This project implements a reusable Python utility module containing commonly used functions for validation, formatting, calculations, and file operations.

The project demonstrates modular programming, code reuse, function documentation, and separation of responsibilities.

## Features

### Validation
- Basic email structure validation
- Positive number validation
- 10-digit phone number validation

### Formatting
- Currency formatting
- Title-case text formatting
- Percentage formatting

### Calculations
- Average calculation
- Factorial calculation
- Percentage calculation

### File Operations
- Read and write text files
- Save Python data as JSON
- Load data from JSON files
- Create parent directories when needed

## Technologies Used
- Python 3
- pathlib
- json
- math

## Project Structure

```text
Day-25-Python-Utility-Module/
├── utility_module.py
├── main.py
├── README.md
├── sample_output.txt
└── demo_data/
    ├── sample.txt
    └── sample.json
```

The `demo_data` directory and its contents are generated automatically when the program runs.

## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python main.py
   ```

4. Review the output demonstrating the utility functions.

## Concepts Practiced
- Creating and importing modules
- Writing reusable functions
- Function documentation using docstrings
- Input validation
- Exception handling
- Numeric calculations
- File handling
- JSON serialization and deserialization
- Using Python standard-library modules

## Future Improvements
- Add more input validation functions.
- Add date and time utilities.
- Add unit tests using unittest or pytest.
- Package the utilities for installation and reuse in other projects.
- Add type hints to function signatures.