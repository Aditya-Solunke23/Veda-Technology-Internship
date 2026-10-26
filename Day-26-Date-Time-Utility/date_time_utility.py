"""
Date and Time Utility Module
Provides functions for age calculation, date differences,
working days, and date/time formatting.
"""

from datetime import date, datetime, time, timedelta


def parse_date(date_string):
    """Convert a YYYY-MM-DD string into a date object."""
    try:
        return datetime.strptime(date_string.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        raise ValueError("Invalid date. Please use YYYY-MM-DD format.")


def calculate_age(birth_date):
    """Calculate age in complete years as of today."""
    if birth_date > date.today():
        raise ValueError("Birth date cannot be in the future.")

    today = date.today()
    age = today.year - birth_date.year

    # Adjust if the birthday has not occurred yet this year.
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def days_between_dates(start_date, end_date):
    """Return the absolute number of days between two dates."""
    return abs((end_date - start_date).days)


def count_working_days(start_date, end_date):
    """
    Count Monday-Friday working days between two dates,
    including both the start and end dates.
    Public holidays are not excluded.
    """
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    working_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            working_days += 1

        current_date += timedelta(days=1)

    return working_days


def format_date(input_date, output_format="%d-%m-%Y"):
    """Format a date using a specified format."""
    return input_date.strftime(output_format)


def format_datetime(input_datetime, output_format="%d-%m-%Y %I:%M %p"):
    """Format a datetime using a specified format."""
    return input_datetime.strftime(output_format)


def add_days(input_date, number_of_days):
    """Return a date after adding the specified number of days."""
    return input_date + timedelta(days=number_of_days)


def get_current_datetime():
    """Return the current local date and time."""
    return datetime.now()


def get_time_difference(start_time, end_time):
    """Return the difference between two datetime objects."""
    return end_time - start_time