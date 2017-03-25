"""
Project Euler Problem 16
Find sum of digits in 2**1000

Program produces correct answer
"""

POWER = 1000

number = 1
for power in range(POWER):
    number = number * 2

number_str = str(number)

number_sum = 0
for digit in range(len(number_str)):
    number_sum += int(number_str[digit])

print(number_sum)