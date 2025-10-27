#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
n=0
x=600851475143
lp=1

while lp!=x:
    if x%lp==0:
        x=x/lp
    lp+=1
print(lp) 