import math
n=int(input())
c=0
add=0
temp=n
d=int(math.log10(n)+1);
while n>0:
    r=n%10
    
    add=add+pow(r,d)
    d-=1
    n=n//10
if add==temp:
    print("True")
else:
    print("False")
    