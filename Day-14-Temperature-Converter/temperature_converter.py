print("========================================")
print("       TEMPERATURE CONVERTER")
print("========================================")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


try:
    print("\nSelect the input temperature unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = input("\nEnter your choice (1-3): ").strip()
    temperature = float(input("Enter the temperature: "))

    if choice == "1":
        if temperature < -273.15:
            print("\nError: Temperature cannot be below absolute zero.")
        else:
            print("\n========== CONVERSION RESULTS ==========")
            print(f"Celsius    : {temperature:.2f} °C")
            print(f"Fahrenheit : {celsius_to_fahrenheit(temperature):.2f} °F")
            print(f"Kelvin     : {celsius_to_kelvin(temperature):.2f} K")
            print("========================================")

    elif choice == "2":
        if temperature < -459.67:
            print("\nError: Temperature cannot be below absolute zero.")
        else:
            print("\n========== CONVERSION RESULTS ==========")
            print(f"Fahrenheit : {temperature:.2f} °F")
            print(f"Celsius    : {fahrenheit_to_celsius(temperature):.2f} °C")
            print(f"Kelvin     : {fahrenheit_to_kelvin(temperature):.2f} K")
            print("========================================")

    elif choice == "3":
        if temperature < 0:
            print("\nError: Kelvin temperature cannot be negative.")
        else:
            print("\n========== CONVERSION RESULTS ==========")
            print(f"Kelvin     : {temperature:.2f} K")
            print(f"Celsius    : {kelvin_to_celsius(temperature):.2f} °C")
            print(f"Fahrenheit : {kelvin_to_fahrenheit(temperature):.2f} °F")
            print("========================================")

    else:
        print("\nError: Invalid choice. Please select 1, 2, or 3.")

except ValueError:
    print("\nError: Please enter a valid numerical temperature.")