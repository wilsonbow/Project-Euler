"""
Project Euler Problem 5
Find smallest even multiple of numbers 1 through 20

Program solves anwer correctly.
Program takes a minute or so to run before solving.
"""

multiple = 20
finished = False
while not finished:
    multiple += 20
    print(multiple)
    for divisor in [19, 18, 17, 16, 15, 14, 13, 12, 11]:
        if multiple % divisor != 0:
            finished = False
            break
        else:
            finished = True

print("The smallest multiple is: {}".format(multiple))
