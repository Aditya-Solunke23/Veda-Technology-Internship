# Day 4 - Student Grade Calculator

print("========================================")
print("        STUDENT GRADE CALCULATOR")
print("========================================")

# Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Validate number of subjects
if num_subjects <= 0:
    print("Error: Number of subjects must be greater than 0.")
else:
    marks = []
    valid_marks = True

    # Taking marks for each subject
    for i in range(1, num_subjects + 1):
        mark = float(input(f"Enter marks for Subject {i} (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Marks must be between 0 and 100.")
            valid_marks = False
            break

        marks.append(mark)

    # Calculate results only if all marks are valid
    if valid_marks:
        total_marks = sum(marks)
        maximum_marks = num_subjects * 100
        percentage = (total_marks / maximum_marks) * 100

        # Assign grade based on percentage
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

        # Display results
        print("\n========== STUDENT RESULTS ==========")
        print(f"Total Marks : {total_marks:g} / {maximum_marks}")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Grade       : {grade}")
        print("======================================")