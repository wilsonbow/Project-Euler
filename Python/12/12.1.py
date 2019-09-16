
number = 0;

def divisor_test(number):
    count = 0;

    for i in range(1, number+1):
        if number % i == 0:
            count += 1;

    return count;

i = 0;
divisors = 1;
while divisors < 500:
    i += 1;
    number += i;
    divisors = divisor_test(number);
    print(number, divisors);
