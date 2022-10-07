n=int(input())
l=list(map(int,input().split()))
arr1=[]
arr2=[]
for i in l:
    if i%2:
        arr1.append(i)
        
        
    else:
        arr2.append(i)
        
arr1.extend(arr2);
print(*arr1)
    