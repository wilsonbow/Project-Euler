
# Lattice paths
# The number of possibilities can be calculated using combinatorics


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def comb(n, k):
    return int(factorial(n)/factorial(n-k)/factorial(k))


def half_lattice(n):
    half = list()
    for i in range(0, n+1):
        half.append(comb(n, i))

    return half


def full_lattice(n):
    count = 0
    for item in half_lattice(n):
        count = count + item * item
    return count


print(full_lattice(20))
