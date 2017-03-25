"""
Project Euler Problem 8
Find the 13 adjacent digits with the largest product in a 1000-digit number.

Program provides correct answer.
"""

file = open('big_number.txt', 'r')

# Retrieve the big number from file
number_list = []
for line in file:
    line = line.strip('\n')
    for char in line:
        number = int(char)
        number_list.append(number)

biggest_product = 0
for i in range(1000-13):    # For each 'set' of 13 numbers
    operands = number_list[i:i+13]
    product = 1

    for j in range(13):     # Find product of 'set'
        product *= operands[j]

    if product > biggest_product:
        biggest_product = product
        biggest_operands = operands

print("The biggest product is: {}".format(biggest_product))