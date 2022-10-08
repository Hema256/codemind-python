def digit(n):
    c=0
    c1=0
    h=n
    while n>0:
        r=n%10
        c+=1
        if r!=0:
            if h%r==0:
                c1+=1
        n=n//10
        
    if c==c1:
        return True
    else:
        return False
a=int(input())
b=int(input())

l=[]
for i in range(a,b+1):
    if digit(i):
        l.append(i)
print(*l)