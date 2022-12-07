from math import *
def isprime(n):
    if n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
h=0
for i in range(2,n//2+1):
    if isprime(i):
        s1=i
    for j in range(2,n//2+1):
        if isprime(j):
            s2=j
            if (s1!=s2):
                if (s1*s2==n):
                    print(s1,s2)
                    h=1
                    break
    if(h==1):
        break
if(h==0):
    print(-1)