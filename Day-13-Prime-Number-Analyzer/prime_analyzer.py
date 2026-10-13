print("========================================")
print("         PRIME NUMBER ANALYZER")
print("========================================")


def is_prime(number):
    """Check whether a number is prime."""
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


# Prime number checker
try:
    number = int(input("\nEnter a number to check: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    # Prime number range generator
    start = int(input("\nEnter the starting value: "))
    end = int(input("Enter the ending value: "))

    if start > end:
        print("\nError: Starting value must be less than or equal to ending value.")
    else:
        prime_numbers = []

        for value in range(start, end + 1):
            if is_prime(value):
                prime_numbers.append(value)

        print("\n========== PRIME NUMBERS ==========")

        if prime_numbers:
            print(f"Prime numbers from {start} to {end}:")
            print(prime_numbers)
        else:
            print(f"No prime numbers found between {start} and {end}.")

        print("===================================")

except ValueError:
    print("\nError: Please enter valid integers.")