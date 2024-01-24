#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
#Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
    # validation to confirm the exp is not negative
    if not isinstance(exp, int) or exp < 0:
        raise ValueError("Exponent must be a non-negative integer")

    result = 1
    
    # main function
    for _ in range(exp):
        result *= base

    return result

# Get user input for base and exponent
try:
    base = int(input("Enter the base (an integer): "))
    exponent_value = int(input("Enter the exponent (a non-negative integer): "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

# Calculate and print the result
result = exponent(base, exponent_value)
print(f"The result of {base} raised to the power of {exponent_value} is: {result}")



