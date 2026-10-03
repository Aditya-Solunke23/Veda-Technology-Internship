# Personal Information Program
# Task 1 - Python Programming Track

print("========================================")
print("       PERSONAL INFORMATION PROFILE")
print("========================================")

# Taking information from the user
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
college = input("Enter your college name: ")
course = input("Enter your course: ")
email = input("Enter your email address: ")

# Displaying the formatted profile
print("\n========================================")
print("             YOUR PROFILE")
print("========================================")

print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"City    : {city}")
print(f"College : {college}")
print(f"Course  : {course}")
print(f"Email   : {email}")

print("========================================")
print("Thank you for providing your information!")
print("========================================")