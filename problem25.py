"""
Project Euler Problem 25
Find first Fibonacci number with more than 1000 digits

Solved!
"""


def find_num_digits(number):
    number_str = str(number)
    return len(number_str)


F = [1, 1]
index = 2

while find_num_digits(F[-1]) < 1000:
    F.append(F[-1] + F[-2])
    index += 1

print("The index of the first 1000 digit Fibonacci number is: {}".format(index))

