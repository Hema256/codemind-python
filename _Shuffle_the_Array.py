n=int(input())
d=list(map(int,input().split()))
d1=[]
j=1
for i in range(0,len(d)):
    if (i<len(d)//2):
        d1.append(d[i])
    else:
        d1.insert(j,d[i])
        j+=2
print(*d1)