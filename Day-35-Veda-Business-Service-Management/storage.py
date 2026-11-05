import json
from pathlib import Path


DATA_FOLDER = Path(__file__).parent / "data"


def load_data(filename):
    file_path = DATA_FOLDER / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print(f"Warning: {filename} contains invalid JSON.")
        return []


def save_data(filename, data):
    file_path = DATA_FOLDER / filename

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError as error:
        print(f"Error saving data: {error}")
        return False