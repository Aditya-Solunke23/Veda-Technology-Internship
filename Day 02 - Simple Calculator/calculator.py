# Day 2 - Simple Calculator

print("========================================")
print("           SIMPLE CALCULATOR")
print("========================================")

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
modulus = num1 % num2

# Displaying results
print("\n========== RESULTS ==========")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")

# Handling division by zero
if num2 != 0:
    division = num1 / num2
    print(f"Division       : {division}")
    print(f"Modulus        : {modulus}")
else:
    print("Division       : Cannot divide by zero")
    print("Modulus        : Cannot calculate modulus with zero")
    
print("==============================")