# Python has functional programming

"""
    Functional programming is when you have a function, but
    you don't need to define it, these functions are called lambda
"""
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Square each number
square_numbers = list(map(lambda x: x ** 2, even_numbers))

# Calculate the sum of squares
sum_of_squares = reduce(lambda x, y: x + y, square_numbers)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Squares of even numbers:", square_numbers)
print("Sum of squares:", sum_of_squares)

# List of tuples where each tuple contains the original number and its square
list_tuple = list(map(lambda x: (x, x ** 2), even_numbers))

print("\nA list of tuples with the original number and its square:", list_tuple)
