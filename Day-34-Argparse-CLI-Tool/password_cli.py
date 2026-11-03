"""
Day 34 - Python Command-Line Tool with argparse
A configurable password generator CLI.
"""

import argparse
import secrets
import string


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    """Generate a secure password using selected character types."""

    character_sets = []

    if use_lower:
        character_sets.append(string.ascii_lowercase)

    if use_upper:
        character_sets.append(string.ascii_uppercase)

    if use_digits:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("Select at least one character type.")

    if length < len(character_sets):
        raise ValueError(
            "Password length must be at least the number of selected character types."
        )

    all_characters = "".join(character_sets)

    # Ensure each selected type appears at least once.
    password_chars = [
        secrets.choice(characters)
        for characters in character_sets
    ]

    # Fill remaining positions.
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_characters))

    # Shuffle to avoid predictable character positions.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    """Parse command-line arguments and generate a password."""

    parser = argparse.ArgumentParser(
        description="Generate a secure password with selected character types."
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Password length (default: 12)"
    )

    parser.add_argument(
        "--lower",
        action="store_true",
        help="Include lowercase letters"
    )

    parser.add_argument(
        "--upper",
        action="store_true",
        help="Include uppercase letters"
    )

    parser.add_argument(
        "--digits",
        action="store_true",
        help="Include digits"
    )

    parser.add_argument(
        "--symbols",
        action="store_true",
        help="Include special characters"
    )

    args = parser.parse_args()

    if args.length < 1:
        parser.error("Password length must be greater than zero.")

    # If no character type is specified, use all types.
    if not any([args.lower, args.upper, args.digits, args.symbols]):
        args.lower = True
        args.upper = True
        args.digits = True
        args.symbols = True

    try:
        password = generate_password(
            args.length,
            args.lower,
            args.upper,
            args.digits,
            args.symbols
        )

        print("Generated Password:")
        print(password)

    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()