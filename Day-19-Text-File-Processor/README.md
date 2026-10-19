
# Day 19 - Read and Process a Text File

## Project Description
A Python program that reads a text file and generates statistics, including line count, word count, and character count.

## Objective
Learn file handling and text processing in Python.

## Technology Used
- Python

## Features
- Reads a text file using `open()`
- Counts lines, words, and characters
- Processes files one line at a time
- Handles missing files
- Handles permission and decoding errors
- Displays formatted statistics

## Concepts Practiced
- File handling
- The `with` statement
- `open()`
- Loops
- String methods
- Counting and accumulation
- Exception handling

## How to Run
Run this command from the project folder:

```bash
python text_processor.py
```

Enter `input.txt` when prompted.

## Interview Questions

### 1. Why should files be opened using `with`?
The `with` statement automatically closes the file when the block finishes, including when an exception occurs.

### 2. What is the difference between read(), readline(), and readlines()?
- `read()` reads the file's contents as a string.
- `readline()` reads one line.
- `readlines()` reads all lines into a list.

### 3. Why is exception handling important when working with files?
It allows the program to handle missing files, permission issues, and decoding errors without terminating unexpectedly.
