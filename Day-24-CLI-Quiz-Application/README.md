# Day 24 – CLI Quiz Application

## Overview
The CLI Quiz Application is a command-line Python program that presents multiple-choice questions, accepts user answers, calculates scores, and displays a final performance summary.

## Features
- Loads questions from a separate JSON file.
- Includes 10 multiple-choice questions.
- Randomizes the order of questions.
- Validates user answers.
- Displays correct answers when a response is incorrect.
- Calculates the final score and percentage.
- Displays a performance summary.
- Handles missing or invalid question data.

## Technologies Used
- Python
- JSON
- random module
- pathlib module

## Concepts Practiced
- Lists and dictionaries
- Loops and conditional statements
- Functions and modular programming
- JSON file handling
- Input validation
- Randomization
- Score calculation and reporting
- Exception handling

## How to Run
1. Install Python 3.
2. Open a terminal in this project directory.
3. Run:

   ```bash
   python quiz_app.py
   ```

4. Select `1` to start the quiz.
5. Answer each question using the displayed options.
6. Review your final score and percentage.

## Project Files
- `quiz_app.py`: Main application logic.
- `questions.json`: Quiz questions, options, and correct answers.
- `README.md`: Project documentation.
- `sample_output.txt`: Example terminal output.

## Future Improvements
- Add different quiz categories.
- Add a timer for each question.
- Save scores and quiz history.
- Add difficulty levels.
- Allow users to create their own quizzes.