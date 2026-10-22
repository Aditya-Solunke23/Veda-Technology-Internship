
# Day 22 - File Organizer

## Project Description
A Python script that scans a selected folder and organizes files into subfolders based on their extensions.

## Objective
Learn filesystem automation using Python.

## Technologies Used
- Python
- pathlib
- shutil

## Features
- Organizes files by extension
- Creates destination folders automatically
- Handles files without extensions
- Prevents duplicate filenames from being overwritten
- Skips directories
- Reports successful and failed moves
- Validates folder paths

## Concepts Practiced
- Filesystem operations
- `pathlib`
- `shutil.move()`
- Loops and conditions
- Functions
- Exception handling
- Path validation

## How to Run
Run:

```bash
python file_organizer.py
```

When prompted, enter the path to your test directory.

Example on Windows:

```text
C:\Users\Aditya\OneDrive\Desktop\Veda Technology\Day-22-File-Organizer\test_directory
```

## Interview Questions

### 1. What is pathlib?
`pathlib` is a Python module that provides an object-oriented way to work with filesystem paths.

### 2. What is the difference between os and shutil?
`os` provides general operating-system interfaces, including filesystem operations. `shutil` provides higher-level file operations such as moving and copying files.

### 3. How can Python automate repetitive file-management tasks?
Python can scan directories, identify files by extension, create folders, and move or rename files automatically.
