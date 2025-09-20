C_CONSTANT = 9/5
F_CONSTANT = 32

# Choose the unit of temperature conversion
unit = input("Choose the unit of temperature conversion (C/F): ").strip().upper()

#take input(Temperature) from the user
temp = float(input("Enter the temperature: "))

# Function to convert Celsius to Fahrenheit
def temp_c_to_f(c):
    return (c*C_CONSTANT) + F_CONSTANT

# Function to convert Fahrenheit to Celsius
def temp_f_to_c(f):
    return (f - F_CONSTANT) * 1/C_CONSTANT

# Check the chosen unit and perform the conversion
if unit == "C":
    converted_temp = temp_c_to_f(temp)
    print(f"{temp}°C is equal to {converted_temp}°F")
elif unit == "F":
    converted_temp = temp_f_to_c(temp)
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid unit. Please choose 'C' or 'F'.")
exit()
    
