"""
Project Euler Problem 12
Find first triangular number to have more than 500 divisors
"""


def find_num_divisors(number):
    num_divisors = 0
    for divisor in range(1, int(number/2+1)):
        if number % divisor == 0:
            num_divisors += 1

    return num_divisors


number = 0
additive = 0
finished = False
while not finished:
    additive += 1
    number += additive
    num_divisors = find_num_divisors(number)
    print("{:10}{:3}".format(number, num_divisors))

    if num_divisors >= 500:
        finished = True

print("The first triangular number with over 500 divisors is: {}".format(number))