


# Function: returns number of digits in integer
def no_digits(number):
    number = abs(number);
    digit = 0;
    check = 2;

    while check > 1:
        digit += 1;
        check = number / (10**digit);

    return digit;

def ispalindrome(number):
    digits = no_digits(number);

    for i in range(1,int(digits/2+1)):
        n1 = int(number / (10**(digits-i)));
        n2 = number % (10**i);

        n1 = n1 % 10**(i-1);
        n2 = int(n2 / 10**i);

        print(n1, n2);



number = int(input("What number do you want to check? "));
print(no_digits(number));
ispalindrome(number);
