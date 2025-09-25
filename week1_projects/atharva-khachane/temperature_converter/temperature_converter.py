def c_to_f(celsius):
    """Converts a temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    """Converts a temperature from Celsius to Kelvin."""
    return celsius + 273.15

def k_to_c(kelvin):
    """Converts a temperature from Kelvin to Celsius."""
    return kelvin - 273.15

def display_menu():
    """Prints the main menu for the user."""
    print("\n--- Temperature Converter Menu ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Please choose an option (1-5): ")

    if choice == '5':
        print("Thank You!!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    try:
        temp_input = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a valid number.")
        continue

    if choice == '1':
        result = c_to_f(temp_input)
        print(f"Result: {temp_input}°C is equal to {result:.2f}°F")
    elif choice == '2':
        result = f_to_c(temp_input)
        print(f"Result: {temp_input}°F is equal to {result:.2f}°C")
    elif choice == '3':
        result = c_to_k(temp_input)
        print(f"Result: {temp_input}°C is equal to {result:.2f}K")
    elif choice == '4':
        result = k_to_c(temp_input)
        if result is None:
            print("Error: Temperature in Kelvin cannot be below absolute zero (0K).")
        else:
            print(f"Result: {temp_input}K is equal to {result:.2f}°C")
