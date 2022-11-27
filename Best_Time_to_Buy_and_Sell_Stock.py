n=int(input())
prices=list(map(int,input().split()))
m=0
h=0
j=prices[0]
for i in range(1,len(prices)):
    if j<prices[i]:
        s=prices[i]-j
        m=max(s,m)
    else:
        if prices.index(prices[i])==len(prices):
            h=1
            print(m)
            break
        else:
            j=prices[i]
if (h==0):
    print(m)
        