import json
import random
from pathlib import Path


QUESTIONS_FILE = Path(__file__).parent / "questions.json"


def load_questions():
    """Load quiz questions from the JSON file."""
    try:
        with QUESTIONS_FILE.open("r", encoding="utf-8") as file:
            questions = json.load(file)

        if not isinstance(questions, list) or not questions:
            raise ValueError("The question file must contain a non-empty list.")

        # Validate the question structure before starting the quiz.
        for question in questions:
            if not isinstance(question, dict):
                raise ValueError("Each question must be a JSON object.")

            if not all(key in question for key in ("question", "options", "answer")):
                raise ValueError("A question is missing a required field.")

            options = question["options"]
            answer = question["answer"]

            if not isinstance(options, dict) or not options:
                raise ValueError("Each question must have answer options.")

            if answer not in options:
                raise ValueError("A correct answer must match one of the options.")

        return questions

    except FileNotFoundError:
        print(f"Error: Could not find {QUESTIONS_FILE.name}.")
    except json.JSONDecodeError:
        print("Error: The questions file contains invalid JSON.")
    except (ValueError, TypeError) as error:
        print(f"Error in question data: {error}")

    return None


def ask_question(question, question_number, total_questions):
    """Display a question and return whether the answer is correct."""
    print(f"\nQuestion {question_number}/{total_questions}")
    print(question["question"])

    for key, value in question["options"].items():
        print(f"  {key}. {value}")

    valid_options = list(question["options"].keys())

    while True:
        answer = input("Your answer: ").strip().upper()

        if answer in valid_options:
            break

        print(
            "Invalid answer. Choose one of these options: "
            + ", ".join(valid_options)
        )

    if answer == question["answer"]:
        print("Correct! ✓")
        return True

    correct_option = question["answer"]
    correct_text = question["options"][correct_option]

    print(f"Incorrect. The correct answer is {correct_option}. {correct_text}")
    return False


def display_result(score, total_questions):
    """Display the final quiz score and performance."""
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)
    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {score}")
    print(f"Incorrect Answers: {total_questions - score}")
    print(f"Final Score     : {score}/{total_questions}")
    print(f"Percentage      : {percentage:.2f}%")

    if percentage >= 80:
        print("Performance     : Excellent!")
    elif percentage >= 60:
        print("Performance     : Good job!")
    elif percentage >= 40:
        print("Performance     : Keep practicing!")
    else:
        print("Performance     : More practice needed.")

    print("=" * 40)


def run_quiz():
    """Run the quiz from start to finish."""
    questions = load_questions()

    if questions is None:
        return

    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    print("\n" + "=" * 40)
    print("          PYTHON CLI QUIZ")
    print("=" * 40)
    print(f"Welcome! This quiz contains {total_questions} questions.")
    print("Choose the correct option: A, B, C, or D.")
    input("\nPress Enter to start the quiz...")

    for number, question in enumerate(questions, start=1):
        if ask_question(question, number, total_questions):
            score += 1

    display_result(score, total_questions)


def main():
    """Application entry point."""
    while True:
        print("\n1. Start Quiz")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Thanks for playing the Python CLI Quiz!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()