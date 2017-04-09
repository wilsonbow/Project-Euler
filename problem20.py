"""
Project Euler Problem 20
Find sum of digits in 100!

Solved!
"""


def digit_sum(number):
    number = str(number)
    total_sum = 0
    for digit in number:
        total_sum += int(digit)

    return total_sum


factorial = 1
for i in range(1, 101):
    factorial *= i


print("The digit sum of {} is: {}".format(str(100), digit_sum(factorial)))
