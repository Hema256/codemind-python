n=int(input())
s=1
for i in range(2,n+1):
    if n%i==0:
        c=0
        j=2
        while j<i:
            if i%j==0:
                c+=1
            j+=1
        if c!=0:
            s+=1
print(s)