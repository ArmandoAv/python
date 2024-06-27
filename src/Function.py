# Python can do functions
"""
    To create a function in python, use the reserved word def
    The function code must have indentation, since Python does 
    not use {} for the beginning and the end of the code
"""

def factorial(n):
    """
        Calculate the factorial of a given number
        Args:
            n (int): Integer number from which the factorial will be calculated
        Returns:
            int: The factorial of the given number
    """

    # Check if the number is an integer
    if not isinstance(n, int):

        raise ValueError(f"{n} isn't an integer")
    
    # Check if the number is a positive integer
    if n < 0:
        raise ValueError("The number must be a positive integer.")

    # Starting the factorial variable
    result = 1
    
    # Calculating the factorial
    for i in range(1, n + 1):
        result *= i
    
    # Return the factorial
    return result

# Calling the function
number = input("Please, enter an integer to calculate its factorial: ")
fact_number = factorial(number)
print(f"The factorial of {number} is {fact_number}")
