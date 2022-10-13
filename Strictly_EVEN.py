n=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in l:
    if i%2==0:
        c+=1
for i in range(len(l)):
    if i%2==0 and l[i]%2==0:
            c1+=1
if c1==c:
    print("True")
else:
    print("False")
