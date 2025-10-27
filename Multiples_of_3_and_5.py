#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
x=0
ans=0
high=1000
while x<high:
    if x%3==0 or x%5==0:
        ans+=x
    x+=1
print('The sum of all the multiples of 3 or 5 below '+str(high)+' is: '+str(ans))