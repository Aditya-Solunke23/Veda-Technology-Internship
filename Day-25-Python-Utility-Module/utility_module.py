"""
Utility Module
--------------
A collection of reusable functions for validation,
formatting, calculations, and file operations.
"""

from pathlib import Path
import json
import math


# ==========================================
# 1. VALIDATION UTILITIES
# ==========================================

def is_valid_email(email):
    """Check whether an email has a basic valid structure."""
    if not isinstance(email, str):
        return False

    email = email.strip()

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    return (
        bool(local)
        and bool(domain)
        and "." in domain
        and not domain.startswith(".")
        and not domain.endswith(".")
        and " " not in email
    )


def is_positive_number(value):
    """Return True if the value is a finite positive number."""
    try:
        number = float(value)
        return math.isfinite(number) and number > 0
    except (ValueError, TypeError):
        return False


def is_valid_phone(phone):
    """Check whether a phone number contains exactly 10 digits."""
    if not isinstance(phone, str):
        return False

    return phone.isdigit() and len(phone) == 10


# ==========================================
# 2. FORMATTING UTILITIES
# ==========================================

def format_currency(amount, currency="INR"):
    """Format a numeric amount as currency."""
    try:
        amount = float(amount)

        if not math.isfinite(amount):
            raise ValueError("Amount must be finite.")

        if currency == "INR":
            return f"₹{amount:,.2f}"
        elif currency == "USD":
            return f"${amount:,.2f}"
        else:
            return f"{currency} {amount:,.2f}"

    except (ValueError, TypeError) as error:
        raise ValueError(
            "Please provide a valid numeric amount."
        ) from error


def format_title(text):
    """Convert text into title case."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    return text.strip().title()


def format_percentage(value, total):
    """Calculate and format a percentage."""
    try:
        value = float(value)
        total = float(total)

        if not math.isfinite(value) or not math.isfinite(total):
            raise ValueError("Values must be finite.")

        if total == 0:
            raise ValueError("Total cannot be zero.")

        percentage = (value / total) * 100
        return f"{percentage:.2f}%"

    except (ValueError, TypeError) as error:
        raise ValueError(
            "Please provide valid numeric values."
        ) from error


# ==========================================
# 3. CALCULATION UTILITIES
# ==========================================

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty.")

    try:
        values = [float(number) for number in numbers]

        if not all(math.isfinite(value) for value in values):
            raise ValueError("All numbers must be finite.")

        return sum(values) / len(values)

    except (ValueError, TypeError) as error:
        raise ValueError(
            "Please provide a list of valid numbers."
        ) from error


def calculate_factorial(number):
    """Calculate the factorial of a non-negative integer."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number < 0:
        raise ValueError(
            "Factorial is not defined for negative integers."
        )

    return math.factorial(number)


def calculate_percentage(value, total):
    """Return a numeric percentage."""
    try:
        value = float(value)
        total = float(total)

        if not math.isfinite(value) or not math.isfinite(total):
            raise ValueError("Values must be finite.")

        if total == 0:
            raise ValueError("Total cannot be zero.")

        return (value / total) * 100

    except (ValueError, TypeError) as error:
        raise ValueError(
            "Please provide valid numeric values."
        ) from error


# ==========================================
# 4. FILE UTILITIES
# ==========================================

def write_text_file(file_path, content):
    """Write text content to a file, creating parent directories."""
    path = Path(file_path)

    if not isinstance(content, str):
        raise TypeError("Content must be a string.")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def read_text_file(file_path):
    """Read and return text from a file."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")


def save_json_file(file_path, data):
    """Save Python data as formatted JSON."""
    path = Path(file_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_json_file(file_path):
    """Load JSON data from a file."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)