n=int(input())
l=list(map(int,input().split()))
m=0
c=0
for i in range(0,len(l)):
    if(l[i]==1):
        c+=1
    else:
        if c>m:
            m=c
        c=0
if c>m:
    m=c
print(m)