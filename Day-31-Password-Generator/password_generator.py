"""
Day 31 - Password Generator
Generate secure, configurable passwords using Python's secrets module.
"""

import secrets
import string


def get_password_length():
    """Ask the user for a valid password length."""
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))

            if length < 4:
                print("Password length must be at least 4.")
            else:
                return length

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_character_options():
    """Ask which character types should be included."""
    print("\nChoose character types:")
    print("1. Lowercase letters")
    print("2. Uppercase letters")
    print("3. Digits")
    print("4. Special characters")

    while True:
        choices = input(
            "Enter choices separated by commas (e.g., 1,2,3,4): "
        ).strip()

        selected = set(choices.replace(" ", "").split(","))

        valid_choices = {"1", "2", "3", "4"}

        if not selected or not selected.issubset(valid_choices):
            print("Invalid selection. Choose from 1, 2, 3, and 4.")
            continue

        character_sets = []

        if "1" in selected:
            character_sets.append(string.ascii_lowercase)

        if "2" in selected:
            character_sets.append(string.ascii_uppercase)

        if "3" in selected:
            character_sets.append(string.digits)

        if "4" in selected:
            character_sets.append(string.punctuation)

        if not character_sets:
            print("Select at least one character type.")
            continue

        return character_sets


def generate_password(length, character_sets):
    """Generate a password containing each selected character type."""
    all_characters = "".join(character_sets)

    # Ensure the password contains at least one character
    # from every selected character type.
    password_characters = [
        secrets.choice(characters)
        for characters in character_sets
    ]

    # Fill the remaining positions securely.
    for _ in range(length - len(password_characters)):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Shuffle characters to avoid predictable placement.
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def main():
    """Run the password generator application."""
    print("=" * 45)
    print("           PASSWORD GENERATOR")
    print("=" * 45)

    length = get_password_length()
    character_sets = get_character_options()

    password = generate_password(length, character_sets)

    print("\n" + "=" * 45)
    print("Generated Password:")
    print(password)
    print("=" * 45)

    print("\nFor security, this application does not save or log passwords.")


if __name__ == "__main__":
    main()