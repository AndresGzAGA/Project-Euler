# -*- coding: utf-8 -*-

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def f(a,b,r):
    '''
    Looks for the biggest palindrome number, lower than p=a*b. After that it defines the biggest 2 divisors a, b of that number p.
    r: Type 'p','a' or 'b' for the function to return the value of that variable. 
    '''
    p=a*b
    while str(p)!=str(p)[::-1]:
        p-=1
    while p%a!=0:
        a-=1
    while (p/a)%b!=0:
        b-=1
    if r=='p':
        return(p)
    elif r=='a':
        return(a)
    elif r=='b':
        return(b)
m=0
n=0
iteration=0
while len(str(f(999-m,999-n,'a')))!=3 or f(999-m,999-n,'p')/(f(999-m,999-n,'a')*f(999-m,999-n,'b'))!=1:
    iteration+=1
    m+=1
    if m==20:
        m=0
        n+=1
a=f(999-m,999-n,'a')
b=f(999-m,999-n,'b')
p=f(999-m,999-n,'p')

print 'On the iteration '+str(iteration)+', with n='+str(n)+' and m='+str(m)+'. The biggest palindrome number is '+str(p)+'='+str(a)+'*'+str(b)