# -*- coding: utf-8 -*-
#The sum of the squares of the first ten natural numbers is,

#1**2 + 2**2 + ... + 10**2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)**2 = 55**2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
suosq=0
sqosu=0
n=0
while n!=100:
    n+=1
    suosq=suosq+n**2
n=0
while n!=100:
    n+=1
    sqosu+=n
sqosu=sqosu**2
print(sqosu-suosq)