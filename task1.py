# Factorial using recursion

# Asking the user for a number
n = int(input('Enter a number: '))

# Performing function using factorial method
def factorial(n):
    if n < 2:
        return 1
    else :
        return n * (factorial(n-1))
    
result = factorial(n)


# Displaying results
print(f"Factorial of {n} is : {factorial(n)}")