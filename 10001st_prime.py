#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?
from math import sqrt

def IsPrime(x):
    '''
    Tests to see if a number x is prime.
    '''
    if x==2 or x==3 or x==5 or x==7:
        return True
    if x%2==0 or x%3==0:
        return False
    n=5
    while n<=sqrt(x):
        if x%n==0:
            return False
        n+=6
    n=7
    while n<=sqrt(x):
        if x%n==0:
            return False
        n+=6
    return True

n=1
x=1
while n!=10001:
    x+=2
    if IsPrime(x)==True:
        n+=1

print 'The '+str(n)+'th number prime is: '+str(x)