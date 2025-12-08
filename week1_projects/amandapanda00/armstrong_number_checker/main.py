# Armstrong Number Checker
# Author: amandapanda00
# Date: 11/04/2025
"""
This program checks whether a given integer is an Armstrong number.

An Armstrong number is equal to the sum of its digits each raised
to the power of the number of digits.
"""


def is_armstrong(number):
    """
    Determine whether a given integer is an Armstrong number.

    An Armstrong number equals the sum of its digits raised to the power
    of the number of digits. Negative numbers automatically return False.

    Parameter:
        number (int): The integer to be tested.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    if number < 0:
        return False  # negative numbers are not Armstrong numbers

    digits = [int(d) for d in str(number)]
    n = len(digits)
    total = sum(d ** n for d in digits)
    return total == number


def process_result(number):
    """Return the formatted Armstrong result string."""
    if is_armstrong(number):
        return f"{number} is an Armstrong number."
    else:
        return f"{number} is not an Armstrong number."


def process_file(filename="numbers.txt"):
    """
    Read lines from a file and test each entry to determine whether it
    is an Armstrong number.

    Invalid lines and empty lines are skipped with an explanation.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()

                if line:
                    try:
                        number = int(line)
                        result = process_result(number)
                        print(result)
                    except ValueError:
                        print(f"Invalid entry on line {line_num}: '{line}'")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Not allowed to read '{filename}'.")


def main():
    """Run the main program menu and input handling."""
    print("Choose input method:")
    print("1. Enter a number using the keyboard")
    print("2. Read a number from a file")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        try:
            num = int(input("Enter a number: "))
            result = process_result(num)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif choice == "2":
        filename = input("Enter filename: ").strip()
        process_file(filename)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
