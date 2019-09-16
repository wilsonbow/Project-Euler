
def pythagoras_hypotenuse(a, b):
    c = sqrt(a**2 + b**2);
    c = check_int(c);
    return c;

def sqrt(y):
    x1 = y/2;

    while 1:
        x2 = x1 - (x1**2 - y)/(2*x1);
        if(abs(x1-x2)<(10**-9)):
            break;
        x1 = x2;

    return x2;

def check_int(x):
    if(abs(x - int(x))<(10**-8)):
        return int(x);
    else:
        return x;

a = 1;
while a < 1000:
    b = a;
    while b <= 1000:
        c = pythagoras_hypotenuse(a,b);
        print(a,b,c);  

        sum = a + b + c;

        # Break immediately if sum > 1000
        if sum > 1000:
            break;
        
        # Check if final condition met
        if sum == 1000:
            print(a*b*c);
            while 1:
                i

        # Add more if number is significantly less  
        if sum < 200:
            b += 100;
        elif sum < 400:
            b += 80;
        elif sum < 600:
            b += 60;
        elif sum < 800:
            b += 40;
        else:
            b += 1;

    a += 1;


            
