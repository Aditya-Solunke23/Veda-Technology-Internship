# Day 5 - Number Guessing Game

## Project Description

This project is a simple Python number guessing game in which the computer generates a random number between 1 and 100.

The user continues guessing until the correct number is found. After every incorrect guess, the program tells the user whether the guess was too high or too low.

The program also keeps track of the number of attempts taken to find the correct answer.

## Objective

The objective of this task is to practice:

- Loops
- Conditional statements
- Random number generation
- User input
- Input validation
- Basic program logic

## Features

- Generates a random number between 1 and 100
- Allows the user to make repeated guesses
- Provides high/low hints
- Counts the number of attempts
- Validates user input
- Stops the game when the correct number is guessed

## How It Works

1. The program generates a random number between 1 and 100 using the `random` module.
2. The user enters a guess.
3. The program compares the guess with the randomly generated number.
4. If the guess is lower, the program displays "Too low".
5. If the guess is higher, the program displays "Too high".
6. The attempt counter is increased after every valid guess.
7. When the correct number is guessed, the program displays the result and number of attempts.
8. The game then ends.

## Example

```text
========================================
          NUMBER GUESSING GAME
========================================

I have selected a number between 1 and 100.
Try to guess the number!

Enter your guess: 40
Too low! Try again.

Enter your guess: 80
Too high! Try again.

Enter your guess: 63

Congratulations! You guessed the correct number.
The number was 63.
Number of attempts: 3
========================================