"""
Project Euler Problem 4
Find the largest palindrome made from the product of two three digit numbers.
"""

# Let the two numbers be a and b
# Increase them one at a time and check product

def is_palindrome(number_str):
    reverse_str = number_str[::-1]

    if number_str == reverse_str:
        return True
    else:
        return False


print(is_palindrome('bob'))