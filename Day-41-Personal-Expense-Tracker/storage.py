import json
from pathlib import Path

# Get the data folder location
DATA_FOLDER = Path(__file__).parent / "data"

# Create the data folder if it doesn't exist
DATA_FOLDER.mkdir(exist_ok=True)


def load_expenses():
    """Load expenses from the JSON file."""

    file_path = DATA_FOLDER / "expenses.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Error: Invalid expense data format.")
                return []

            return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Expense file contains invalid JSON.")
        return []

    except OSError as error:
        print(f"Error loading expenses: {error}")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""

    file_path = DATA_FOLDER / "expenses.json"

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

        return True

    except (OSError, TypeError) as error:
        print(f"Error saving expenses: {error}")
        return False