"""
Project Euler Problem 14
Find longest Collatz sequence chain under 1 million

Program produces correct answer
"""

def collatz(number):
    if number % 2 == 0: # number even
        number /= 2
    else: #number odd
        number = 3 * number + 1

    return number


longest_chain = 0
longest_chain_num = 0
for i in range(1, 1000000+1):
    chain = 0
    number = i
    print(i)
    while number != 1:
        number = collatz(number)
        chain += 1

    if chain > longest_chain:
        longest_chain = chain
        longest_chain_num = i

print("The longest Collatz sequence is produced by: {}".format(longest_chain_num))