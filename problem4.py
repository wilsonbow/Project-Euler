"""
Project Euler Problem 4
Find the largest palindrome made from the product of two three digit numbers.

Correct answer found using this program.
"""


def is_palindrome(number_str):
    reverse_str = number_str[::-1]

    if number_str == reverse_str:
        return True
    else:
        return False


# Let the two numbers be a and b
# Increase them one at a time and check product
largest_palindrome = 0
for a in range(100, 1000):
    for b in range(a, 1000):
        c = a * b
        if is_palindrome(str(c)) and c > largest_palindrome:
            largest_palindrome = c

print("The largest palindrome created as a product of two three-digit numbers is: {}".format(largest_palindrome))
