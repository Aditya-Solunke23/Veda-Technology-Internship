"""
Day 33 - Python Project With Logging
A simple student records manager with structured logging.
"""

import logging


# Configure logging to write messages to app.log
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

students = {}


def add_student(student_id, name, marks):
    """Add a student record."""
    if student_id in students:
        logger.warning("Student ID %s already exists.", student_id)
        return False

    if not name.strip():
        logger.error("Cannot add student with an empty name.")
        return False

    if not 0 <= marks <= 100:
        logger.error("Invalid marks entered for student ID %s.", student_id)
        return False

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    logger.info("Student %s added successfully.", student_id)
    return True


def view_student(student_id):
    """Return a student record if it exists."""
    student = students.get(student_id)

    if student is None:
        logger.warning("Student ID %s was not found.", student_id)
        return None

    logger.info("Student record %s viewed.", student_id)
    return student


def calculate_grade(marks):
    """Return a grade based on marks."""
    if not 0 <= marks <= 100:
        logger.error("Cannot calculate grade: marks must be between 0 and 100.")
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def main():
    """Run a sample student records workflow."""
    logger.info("Student Manager application started.")

    add_student(101, "Aarav", 85)
    add_student(102, "Meera", 92)

    # Demonstrate a warning: duplicate student ID
    add_student(101, "Aarav", 85)

    # Demonstrate a warning: missing student
    view_student(999)

    # Demonstrate an error: invalid marks
    add_student(103, "Kabir", 120)

    student = view_student(101)

    if student:
        grade = calculate_grade(student["marks"])
        logger.info(
            "Grade calculated for student ID %s: %s",
            101,
            grade
        )

    logger.info("Student Manager application finished.")


if __name__ == "__main__":
    main()