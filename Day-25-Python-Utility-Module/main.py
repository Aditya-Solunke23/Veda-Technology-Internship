"""
Main Program
------------
Demonstrates how to use the reusable utility module.
"""

from pathlib import Path
import utility_module as utils


def main():
    """Run examples of the utility functions."""

    print("=" * 50)
    print("       PYTHON UTILITY MODULE DEMO")
    print("=" * 50)

    # ==========================================
    # 1. VALIDATION UTILITIES
    # ==========================================

    print("\n1. VALIDATION UTILITIES")

    print(
        "Email validation:",
        utils.is_valid_email("student@example.com")
    )

    print(
        "Positive number validation:",
        utils.is_positive_number(150)
    )

    print(
        "Phone validation:",
        utils.is_valid_phone("9876543210")
    )

    # ==========================================
    # 2. FORMATTING UTILITIES
    # ==========================================

    print("\n2. FORMATTING UTILITIES")

    print(
        "Currency:",
        utils.format_currency(12345.5)
    )

    print(
        "Title:",
        utils.format_title("python utility module")
    )

    print(
        "Formatted percentage:",
        utils.format_percentage(45, 60)
    )

    # ==========================================
    # 3. CALCULATION UTILITIES
    # ==========================================

    print("\n3. CALCULATION UTILITIES")

    print(
        "Average:",
        utils.calculate_average([10, 20, 30, 40, 50])
    )

    print(
        "Factorial of 5:",
        utils.calculate_factorial(5)
    )

    print(
        "Numeric percentage:",
        utils.calculate_percentage(25, 100)
    )

    # ==========================================
    # 4. FILE UTILITIES
    # ==========================================

    print("\n4. FILE UTILITIES")

    # Create demonstration files inside the project directory.
    demo_folder = Path(__file__).parent / "demo_data"

    text_file = demo_folder / "sample.txt"
    json_file = demo_folder / "sample.json"

    # Demonstrate writing and reading a text file.
    utils.write_text_file(
        text_file,
        "Hello! This file was created using our utility module."
    )

    print("Text file content:")
    print(utils.read_text_file(text_file))

    # Demonstrate saving and loading JSON data.
    sample_data = {
        "name": "Student",
        "course": "Python Programming",
        "completed_day": 25
    }

    utils.save_json_file(json_file, sample_data)

    print("\nJSON data:")
    print(utils.load_json_file(json_file))

    print("\n" + "=" * 50)
    print("       DEMONSTRATION COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()