# Day 6 - Multiplication Table

print("========================================")
print("         MULTIPLICATION TABLE")
print("========================================")

# Taking input from the user
number = int(input("Enter the number: "))
limit = int(input("Enter the table limit: "))

# Validate the limit
if limit <= 0:
    print("Error: The table limit must be greater than 0.")
else:
    print(f"\nMultiplication Table of {number}")
    print("----------------------------------------")

    # Generate multiplication table
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

    print("========================================")