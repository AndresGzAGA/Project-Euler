#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

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

l=2000000
r=2
x=3
while x<l:
    if IsPrime(x)==True:
        r+=x
    x+=2

print 'The sum of all primes below '+str(l)+' is: '+str(r)