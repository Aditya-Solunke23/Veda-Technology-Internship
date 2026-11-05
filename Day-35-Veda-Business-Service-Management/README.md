# Day 35 – Veda Technology Business & Service Management System

## Overview

A menu-driven Python application designed to manage business services,
technology programs, training programs, internship programs, customer
inquiries, and service requests.

The application stores records in JSON files, allowing data to persist
after the program is closed.

## Features

### Digital Services
- Add digital services
- View services
- Search services
- Store service name, category, description, price, and status

### Program Management
- Add technology programs
- Add training programs
- Add internship programs
- View and search programs
- Update program status

### Customer Inquiry Management
- Add customer inquiries
- View inquiries
- Search inquiries
- Update inquiry status

### Service Request Management
- Add service requests
- Assign priority levels
- View and search requests
- Update request status

### Search and Reports
- Search across all application records
- Generate business summaries
- View totals and status-based counts

## Technologies Used

- Python 3
- JSON
- pathlib
- Functions and classes
- File handling
- Exception handling

## Project Structure

- `main.py` – Main application menu
- `models.py` – Data models
- `storage.py` – JSON file handling
- `services.py` – Digital service management
- `programs.py` – Program management
- `inquiries.py` – Customer inquiry management
- `requests.py` – Service request management
- `search.py` – Search across all records
- `reports.py` – Business reports
- `data/` – JSON data storage

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal in the project folder.
4. Run:

```bash
python main.py