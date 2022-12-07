import math
def digit(n):
    s=0
    while n>0:
        r=n%10
        s=s+math.pow(r,2)
        n=n//10
    return s
n=int(input())
j=0
r=n
h=0
for i in range(n):
    r=digit(r)
    if (r==1 or r==7):
        h=1
        print("True")
        break
if h==0:
    print("False")