
# Day 21 - JSON Data Processor

## Project Description
A Python program that reads employee records from a JSON file and supports searching, filtering, salary summaries, and saving filtered results.

## Objective
Learn JSON handling and structured data processing.

## Technologies Used
- Python
- json module

## Features
- Loads employee records from JSON
- Displays employee information
- Searches employees by name
- Filters employees by department
- Calculates minimum, maximum, and average salary
- Saves filtered records to a new JSON file
- Validates required employee fields
- Handles missing files and malformed JSON

## Concepts Practiced
- `json.load()` and `json.dump()`
- Dictionaries and lists
- List comprehensions
- Functions
- Data validation
- File handling
- Exception handling

## How to Run
Keep `data.json` and `json_processor.py` in the same directory, then run:

```bash
python json_processor.py
```

## Interview Questions

### 1. What is JSON?
JSON stands for JavaScript Object Notation. It is a text-based format used to store and exchange structured data.

### 2. What is the difference between JSON and a Python dictionary?
JSON is a text-based data format. A Python dictionary is an in-memory data structure. The `json` module converts between JSON data and compatible Python objects.

### 3. How do you read JSON from a file in Python?
Use `json.load(file)` after opening the file in read mode.

### 4. What is the difference between `json.load()` and `json.dump()`?
`json.load()` reads JSON data from a file, while `json.dump()` writes Python data to a JSON file.
