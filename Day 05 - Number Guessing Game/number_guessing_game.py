# Day 5 - Number Guessing Game

import random

print("========================================")
print("          NUMBER GUESSING GAME")
print("========================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Try to guess the number!")

# Continue until the correct number is guessed
while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    # Validate the guessing range
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\nCongratulations! You guessed the correct number.")
        print(f"The number was {secret_number}.")
        print(f"Number of attempts: {attempts}")
        print("========================================")
        break