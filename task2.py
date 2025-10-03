import math

# Ask the user for a number
number = float(input('Enter your number: '))

# Perform calculations using math module
square = math.sqrt(number)
log = math.log(number)
sine = math.sin(number)

# Display results
print(f"Square root of {number} is : {square}")
print(f"Natural logarithm of {number} is : {log}")
print(f"Sine of {number} is : {sine}")

