# Armstrong Number Checker
# Author: amandapanda00
# Date: 11/04/2025

"""
This program checks whether a given integer is an Armstrong number.

An Armstrong number is equal to the sum of the cubes of its digits.
"""


def is_armstrong(number):
    """
    Determine whether a given integer is an Armstrong number.

    Parameter:
        number (int): The integer to be tested.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(number)]
    n = len(digits)  # number of digits
    # og had ** 3
    # change to n to accommodate armstrong numbers more than 3 digits
    total = sum(d ** n for d in digits)
    return total == number


def process_result(number):
    """Print the result."""
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")


def process_file(filename="numbers.txt"):
    """
    Read multiple lines from a file and check each one.

    See if it is an Armstrong number.
    """
    try:
        with open(filename, "r") as file:
            # read only to keep integrity of data
            for line_num, line in enumerate(file, start=1):
                # loop through data in file
                # number each line in file starting with 1
                # keep track of bad data
                line = line.strip()
                # removes newline ect. cleans line

                # Only process the line if it is not empty
                if line:
                    try:
                        number = int(line)
                        process_result(number)
                    except ValueError:
                        print(f"Invalid entry on line {line_num}: '{line}'")
                # If the line is empty do nothing
                # print error for user clarity

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Not allowed to read '{filename}'.")


def main():
    """Run main."""
    print("Choose input method:")
    print("1. Enter a number using the keyboard")
    print("2. Read a number from a file")
    # print user menu

    choice = input("Enter choice (1 or 2): ").strip()
    # get user choice
    # strip cleans input-user errors, extra spaces

    if choice == "1":
        try:
            num = int(input("Enter a number: "))
            # string to int
            process_result(num)
            # call function
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            # value error to fail gracefully. abc != 123

    elif choice == "2":
        filename = input("Enter filename: ").strip()
        process_file(filename)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
