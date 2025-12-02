Amandapanda00 – Armstrong Number Checker
What the project does: 
This project determines whether a given integer is an Armstrong number—a number equal to the sum of the cubes of its digits equals the number itself (153 = 1³ + 5³ + 3³ = 153).

How to run it:
1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project in an environment that supports Python such as VS code or PyCharm.
4. Run the `main.py` file.
5. When prompted, choose an input method:

* Keyboard input: Enter a number directly.

* File input: Enter a filename to check numbers from a file (e.g., numbers.txt). 
  The program will read each line and check if it is an Armstrong number. 
  Invalid lines are skipped with a message for the user.

Example input/output

Example Input:

153

Expected Output:

153 is an Armstrong number

Another Example:

numbers.txt file

Line 1: abc: Raises a ValueError when converting to int. The program prints:
Invalid entry on line 1: 'abc'

Line 2: 123 = Successfully converted to an integer. Checked by is_armstrong(). Output:
123 is not an Armstrong number.

Line 3: 153 = Successfully converted to an integer. Checked by is_armstrong(). Output:
153 is an Armstrong number.

Line 4: 370 = Successfully converted to an integer. Checked by is_armstrong(). Output:
370 is an Armstrong number.

Line 5: 456 = Successfully converted to an integer. Checked by is_armstrong(). Output:
456 is not an Armstrong number.

Line 6: xyz  Raises a ValueError. Output:
Invalid entry on line 6: 'xyz'

Line 7: 9474 = Successfully converted to an integer. Checked by is_armstrong(). Output:
9474 is an Armstrong number.

This file demonstrates:

* Try/except blocks catching invalid data (abc and xyz).

* Data integrity: only valid numbers are processed. File "r" read only.

* File handling: reads multiple lines from a file.


Error Handling

try/except blocks are used to handle invalid input/value errors.

* This ensures the program is not going to crash if a user enters a non-integer value.

* When reading a file, invalid entries are skipped, and the line number is reported to help track and identify errors.

* File handling is done with "r" mode (read-only) to protect the file and prevent accidental changes.


Testing

* PyCharm Debugger: Used to step through code and verify logic.

* Pytest: Automatically tests the functionality of the Armstrong Number Checker, including both keyboard input and file input. Ensures that the program behaves     correctly for a variety of cases.

* Flake8: Checks code against Python style guidelines (PEP 8).

* Pydocstyle: Checks that documentation is complete and clear, ensuring maintainability.



