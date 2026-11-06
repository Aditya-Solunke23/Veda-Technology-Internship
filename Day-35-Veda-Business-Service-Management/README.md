# Veda Technology Business & Service Management System

A Python-based, menu-driven Business & Service Management System developed as part of my Veda Technology Python Programming Internship.

The application is designed to manage the operations of a technology and digital-services organization, including digital services, technology and training programs, internship programs, customer inquiries, and service requests.

The project applies Object-Oriented Programming, Modular Programming, and JSON-based data storage to create an organized and maintainable application.

---

## Project Development Timeline

### Day 1 – Project Planning & Core Module Development
**Internship Day 35**

The first day focused on understanding the project requirements, planning the application architecture, and developing its foundational components.

**Work Completed:**
- Planned the overall application structure and functionality.
- Created the project directory and modular file structure.
- Created Python classes for digital services, programs, customer inquiries, and service requests.
- Developed the Digital Service Management module.
- Developed the Technology, Training, and Internship Program Management module.
- Implemented the initial JSON-based data storage structure.

**Concepts Applied:** Python OOP, Classes and Objects, Functions, Modules, Lists, Dictionaries, and JSON.

### Day 2 – Module Development & Application Integration
**Internship Day 36**

The second day focused on developing the remaining management modules and connecting them to the main application.

**Work Completed:**
- Developed the Customer Inquiry Management module.
- Implemented adding, viewing, searching, and updating customer inquiries.
- Developed the Service Request Management module.
- Implemented service request priorities and status management.
- Integrated all management modules into the main application menu.
- Developed search functionality across different categories of records.
- Implemented a business reporting module to display important record statistics.

**Concepts Applied:** Modular Programming, OOP, JSON File Handling, Data Management, Searching, and Application Integration.

### Day 3 – Application Testing & Verification
**Internship Day 37**

The third day focused on testing the integrated application and verifying that its different functionalities worked together correctly.

**Work Completed:**
- Tested the complete application through the main menu.
- Verified digital service and program management operations.
- Tested customer inquiry creation and status updates.
- Tested service request creation, priority selection, and status updates.
- Verified search functionality across all records.
- Tested business reports and record statistics.
- Checked JSON-based data persistence by restarting the application.
- Reviewed the overall project structure.

**Concepts Applied:** Application Testing, Debugging, Exception Handling, File Handling, Modular Programming, and Data Persistence.

### Day 4 – Final Refinement & Project Completion
**Internship Day 38**

The fourth day focused on reviewing the complete project, consolidating the developed modules, and preparing the application for final submission.

**Work Completed:**
- Reviewed the overall application architecture and project organization.
- Performed a final review of the individual management modules.
- Checked the integration between the main menu and supporting modules.
- Reviewed the JSON data storage structure and persistence workflow.
- Consolidated the project documentation and development timeline.
- Organized the final project files and GitHub submission structure.
- Prepared the project for final demonstration and submission.

**Concepts Applied:** Project Organization, Code Review, Application Integration, Documentation, Testing, and Version Control using Git.

---

## Key Features

- **Digital Service Management:** Add, view, and search digital services.
- **Program Management:** Manage technology, training, and internship programs.
- **Customer Inquiry Management:** Maintain customer inquiries and update their statuses.
- **Service Request Management:** Create and manage service requests with different priorities.
- **Search Functionality:** Search across multiple categories of records.
- **Business Reports:** View basic statistics about services, programs, inquiries, and service requests.
- **Persistent Data Storage:** Store application records using JSON files.

## Technologies Used

- Python
- JSON
- Object-Oriented Programming
- Modular Programming
- File Handling
- Exception Handling
- Git and GitHub

## Project Structure

```text
Day-37-Veda-Business-Service-Management/
│
├── main.py
├── models.py
├── storage.py
├── services.py
├── programs.py
├── inquiries.py
├── requests.py
├── search.py
├── reports.py
│
├── data/
│   ├── services.json
│   ├── programs.json
│   ├── inquiries.json
│   └── requests.json
│
├── README.md
└── sample_output.txt
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/Aditya-Solunke23/Veda-Technology-Internship.git
```

**2. Navigate to the project directory**

```bash
cd Veda-Technology-Internship/Day-37-Veda-Business-Service-Management
```

**3. Run the application**

```bash
python main.py
```

## Data Storage

The application uses JSON files to store information about digital services, programs, customer inquiries, and service requests.

This allows records to remain available even after the application is closed and restarted.

## Learning Outcomes

Through this four-day project, I gained practical experience in:

- Designing and developing a modular Python application.
- Applying Object-Oriented Programming principles.
- Managing structured data using JSON.
- Working with multiple Python modules.
- Implementing search and reporting functionalities.
- Handling user input and exceptions.
- Testing and integrating different application components.
- Organizing and documenting a complete software project.

## Future Enhancements

- Database integration using MySQL or SQLite.
- User authentication and role-based access.
- Graphical User Interface (GUI).
- Advanced reporting and analytics.
- Exporting reports to CSV or PDF.

---

**Developed by:** Aditya Solunke

**Internship:** Veda Technology – Python Programming Internship

**Project:** Business & Service Management System

**Project Duration:** 4 Days