# Day 9 - Student Records Using Lists

print("========================================")
print("         STUDENT RECORD SYSTEM")
print("========================================")

# Student names and corresponding marks
names = ["Aditya", "Rahul", "Sneha", "Priya", "Rohan"]
marks = [85, 72, 91, 68, 78]

# Display all student records
print("\n========== STUDENT RECORDS ==========")

for i in range(len(names)):
    print(f"{i + 1}. {names[i]} - {marks[i]} marks")

# Find highest and lowest marks
highest_mark = max(marks)
lowest_mark = min(marks)

highest_index = marks.index(highest_mark)
lowest_index = marks.index(lowest_mark)

print("\n========== SCORE DETAILS ==========")
print(f"Highest Score : {highest_mark} - {names[highest_index]}")
print(f"Lowest Score  : {lowest_mark} - {names[lowest_index]}")

# Search for a student
search_name = input("\nEnter a student name to search: ").strip()

if search_name in names:
    student_index = names.index(search_name)
    print(
        f"{names[student_index]} has scored "
        f"{marks[student_index]} marks."
    )
else:
    print("Student not found.")

# Sort records by marks
sorted_records = sorted(zip(names, marks), key=lambda record: record[1], reverse=True)

print("\n========== SORTED BY MARKS ==========")

for rank, (name, mark) in enumerate(sorted_records, start=1):
    print(f"{rank}. {name} - {mark} marks")

print("====================================")