Day 37 – Project Development Report
Veda Technology Business & Service Management System
Internship: Veda Technology – Python Programming Internship
Internship Day: 37
Project Day: 3 of 4
Developer: Aditya Solunke  
1. Project Overview
The Veda Technology Business & Service Management System is a menu-driven Python application designed to represent the operations of a technology and digital-services organization.

The application manages digital services, technology and training programs, internship programs, customer inquiries, and service requests. It uses modular Python files and JSON files to organize and persist application data.
2. Objectives for Project Day 3
The focus of the third project day was to verify the integrated application, check that its modules work together, and review its data-storage workflow.

The intended checks included:
- Running the application through its main menu.
- Checking access to the service, program, inquiry, and service-request modules.
- Reviewing search and reporting functionality.
- Checking that application records are stored in JSON files.
- Reviewing the project structure and documentation.
3. Application Modules
Module	Responsibility
main.py	Displays the main menu and connects the application modules.
models.py	Defines classes for services, programs, inquiries, and service requests.
storage.py	Loads and saves JSON data.
services.py	Manages digital service records.
programs.py	Manages technology, training, and internship programs.
inquiries.py	Manages customer inquiries and their statuses.
requests.py	Manages service requests, priorities, and statuses.
search.py	Searches across stored application records.
reports.py	Displays basic business statistics.


4. Functional Areas Reviewed
Digital Service Management
The service module supports maintaining digital service records, including adding, viewing, and searching services.
Program Management
The program module supports managing technology, training, and internship program records.
Customer Inquiry Management
The inquiry module supports creating, viewing, searching, and updating customer inquiry statuses.
Service Request Management
The service-request module supports creating and viewing requests, assigning priorities, searching records, and updating request statuses.
Search and Business Reports
The application includes a search facility for locating records across modules and a reporting facility for displaying summary counts and statuses.
5. Data Storage
The application uses JSON files for persistent storage:
- services.json
- programs.json
- inquiries.json
- requests.json
The storage module is responsible for loading records when needed and saving updates to the corresponding files. JSON storage keeps the project lightweight and makes the data readable during development.
6. Testing and Verification Checklist
Mark an item only after you have personally run and verified it.
- [ ] Application starts successfully using python main.py.
- [ ] Main menu opens each management module.
- [ ] A digital service can be added and viewed.
- [ ] A program can be added and viewed.
- [ ] A customer inquiry can be added and its status updated.
- [ ] A service request can be added and its status updated.
- [ ] Search returns matching records.
- [ ] Business reports display the available record summaries.
- [ ] Records remain available after closing and restarting the application.
- [ ] Invalid menu choices and missing records are handled appropriately.
7. Concepts Used
- Python functions and modules
- Object-Oriented Programming
- Classes and objects
- Lists and dictionaries
- JSON serialization and deserialization
- File handling
- Input validation and exception handling
- Searching and basic reporting
- Modular application design
8. Outcome
The project brings together multiple management modules in a single menu-driven Python application. The Day 3 work focused on reviewing the integration and checking the application's end-to-end workflow and data persistence.

The checklist above should be completed based on actual test results before this report is submitted.
9. How to Run
From the project directory, run:
python main.py
10. Project Repository
GitHub: https://github.com/Aditya-Solunke23/Veda-Technology-Internship/tree/main/Day-37-Veda-Business-Service-Management
Note: This report documents the project structure and the Day 3 verification plan. Only mark testing checklist items as complete when the corresponding test has been run successfully.