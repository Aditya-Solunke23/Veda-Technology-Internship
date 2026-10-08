# Day 8 - Simple To-Do List

tasks = []


def add_task():
    task = input("Enter the task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("================================")


def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter the task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ").strip()

            if new_task:
                tasks[task_number - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid task number.")


def remove_task():
    if not tasks:
        print("\nNo tasks available to remove.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter the task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid task number.")


def display_menu():
    print("\n========================================")
    print("           SIMPLE TO-DO LIST")
    print("========================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")
    print("========================================")


# Main program
while True:
    display_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print("\nThank you for using the To-Do List!")
        print("========================================")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 5.")