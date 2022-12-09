n=int(input())
d="1234567890"
while n>0:
    a=input()
    h=0
    for i in a:
        if i in d:
            h=1
            print("Yes")
            break
    if h==0:
        print("No")