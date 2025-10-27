#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a**2 + b**2 = c**2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.



from math import sqrt

def nsq(n,ab):
    '''
    Returns the nth set of numbers a,b so that a**2 +b**2 = a c**2, a perfect square.
    Specify if you want the function to return the number a or the number b
    '''
    a=0.0
    b=0.0
    t=0
    if n==0:
        return 0
    while True:
        a+=1
        #print(a)
        for b in range(1,int(a+1)):
            #print(b)
            if (sqrt(a**2+b**2)).is_integer():
                t+=1
                if t==n:
                    if ab=='a':
                        return(a)
                    elif ab=='b':
                        return(b)

n=0
a=0
b=0
c=0
while (a+b+c)!=1000:
    a=nsq(n,'a')
    b=nsq(n,'b')
    c=sqrt(a**2+b**2)
    n+=1
print 'The triplet is '+str(a)+'+'+str(b)+'+'+str(c)+'=1000, and the product of the triplet is a*b*c='+str(a*b*c)