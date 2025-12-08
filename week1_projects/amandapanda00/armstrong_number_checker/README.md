Amandapanda00 – Armstrong Number Checker
What the project does: 
This project determines whether a given integer is an Armstrong number. An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits. (153 = 1³ + 5³ + 3³ = 153).

The program allows you to:

* Enter numbers directly from the keyboard, or

* Read and process multiple numbers from a file.

It includes proper error handling, file-processing safety, and clear output formatting.

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

Line 8: -45 = Successfully converted to an integer. Checked by is_armstrong(). Output:
-45 is not an Armstrong number.

Line 9: -153 = Successfully converted to an integer. Checked by is_armstrong(). Output:
-153 is not an Armstrong number.

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

Updates Included in This Version

1. process_result() now returns a string instead of printing directly. This improves testability and separation of concerns.

2. main() is updated so all printing happens in one place, following recommended best practices.

3. Improved documentation for clarity.

4. Updated file-processing function to include:
* Files are opened using encoding="utf-8" to ensure proper handling of characters in different environments and locales.

* This prevents issues with non-ASCII characters and ensures consistent behavior across operating systems.


Future Improvements / Suggestions

Here are recommended enhancements that could be added:


* Add GUI version 

* Limit maximum allowed digits/value to avoid CPU/memory DoS from huge inputs and report if input is too large.

* Expand pytest coverage to include file-processing tests

* Add a GitHub Actions workflow 



