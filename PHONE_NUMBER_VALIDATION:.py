n=int(input())
s=str(n)
l=list(s)
if len(l)==10 and n//10!=0:
    print("Valid")
else:
    print("Invalid")