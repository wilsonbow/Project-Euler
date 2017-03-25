"""
Project Euler Problem 13
Find first ten digits of sum of heaps of numbers

Program produces correct answer
"""

file = open('big_number_13.txt', 'r')

num_sum = 0
for line in file:
    line = line.strip()
    num_sum += int(line)

num_sum_str = str(num_sum)

print("The first ten numbers of the sum are: {}".format(num_sum_str[0:10]))