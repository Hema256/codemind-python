n=int(input())
while n>0:
    a=int(input())
    rev=0
    temp=a
    while a>0:
        r=a%10
        rev=rev*10+r
        a=a//10
    if rev==temp:
        print("True")
    else:
        print("False")
        
    n-=1