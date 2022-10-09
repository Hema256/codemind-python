def rev(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
sq=n*n
n1=rev(n)
sq1=n1*n1
sq2=rev(sq1)
if sq==sq2:
    print("True")
else:
    print("False")