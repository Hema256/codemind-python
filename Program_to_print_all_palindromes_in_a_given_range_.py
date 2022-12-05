def palin(n):
    rev=0
    temp=n
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==temp:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if palin(i):
        print(i,end=" ")