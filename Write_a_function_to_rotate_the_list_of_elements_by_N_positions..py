n=int(input())
d=list(map(int,input().split()))
k=int(input())
for i in range(0,k):
    a=d[-1]
    d.reverse()
    d.remove(a)
    d.reverse()
    d.insert(0,a)
print(*d)
    