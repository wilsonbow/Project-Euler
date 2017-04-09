"""
Project Euler Problem 12
Find first triangular number to have more than 500 divisors
"""

from math import sqrt


def find_num_divisors(number):
    num_divisors = 0
    for divisor in range(1, int(sqrt(number))+1):
        if number % divisor == 0:
            num_divisors += 2

    if sqrt(number) % 1 == 0:
        num_divisors -= 1

    return num_divisors


number = 0
additive = 0
finished = False
while not finished:
    additive += 1
    number += additive
    num_divisors = find_num_divisors(number)
    print("{:10}{:4}".format(number, num_divisors))

    if num_divisors >= 10:
        finished = True

print("The first triangular number with over 500 divisors is: {}".format(number))