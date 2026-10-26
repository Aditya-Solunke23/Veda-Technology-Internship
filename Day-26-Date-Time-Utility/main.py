"""
Date and Time Utility Application
Interactive menu for date calculations.
"""

from datetime import datetime, date
import date_time_utility as utils


def main():
    while True:
        print("\n" + "=" * 45)
        print("         DATE AND TIME UTILITY")
        print("=" * 45)
        print("1. Calculate Age")
        print("2. Calculate Days Between Dates")
        print("3. Count Working Days")
        print("4. Format a Date")
        print("5. Add Days to a Date")
        print("6. Display Current Date and Time")
        print("7. Calculate Time Difference")
        print("8. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                birth_input = input(
                    "Enter your birth date (YYYY-MM-DD): "
                )
                birth_date = utils.parse_date(birth_input)
                age = utils.calculate_age(birth_date)

                print(f"Your age is {age} years.")

            elif choice == "2":
                start = utils.parse_date(
                    input("Enter the first date (YYYY-MM-DD): ")
                )
                end = utils.parse_date(
                    input("Enter the second date (YYYY-MM-DD): ")
                )

                difference = utils.days_between_dates(start, end)
                print(f"Difference: {difference} days.")

            elif choice == "3":
                start = utils.parse_date(
                    input("Enter the start date (YYYY-MM-DD): ")
                )
                end = utils.parse_date(
                    input("Enter the end date (YYYY-MM-DD): ")
                )

                working_days = utils.count_working_days(start, end)
                print(f"Working days: {working_days}")

                print(
                    "Note: Saturdays and Sundays are excluded; "
                    "public holidays are not."
                )

            elif choice == "4":
                input_date = utils.parse_date(
                    input("Enter a date (YYYY-MM-DD): ")
                )

                print(
                    "Formatted date:",
                    utils.format_date(input_date, "%d %B %Y")
                )

            elif choice == "5":
                input_date = utils.parse_date(
                    input("Enter a date (YYYY-MM-DD): ")
                )
                days = int(input("Enter the number of days to add: "))

                result = utils.add_days(input_date, days)
                print("Result:", utils.format_date(result, "%d-%m-%Y"))

            elif choice == "6":
                current = utils.get_current_datetime()

                print(
                    "Current date and time:",
                    utils.format_datetime(current)
                )

            elif choice == "7":
                start_text = input(
                    "Enter start date and time (YYYY-MM-DD HH:MM): "
                )
                end_text = input(
                    "Enter end date and time (YYYY-MM-DD HH:MM): "
                )

                start = datetime.strptime(
                    start_text.strip(), "%Y-%m-%d %H:%M"
                )
                end = datetime.strptime(
                    end_text.strip(), "%Y-%m-%d %H:%M"
                )

                difference = utils.get_time_difference(start, end)
                print("Time difference:", difference)

            elif choice == "8":
                print("Thank you for using Date and Time Utility!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 8.")

        except ValueError as error:
            print("Input error:", error)

        except OverflowError:
            print("Error: The date calculation exceeds the supported range.")


if __name__ == "__main__":
    main()