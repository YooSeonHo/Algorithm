import sys
input = sys.stdin.readline

n = int(input())
price = []
for _ in range(n):
    price.append(int(input()))

price.sort(reverse=True)
res = 0

if n == 1 :
    res += price[0]
elif n == 2:
    res = res +  price[0] + price[1]
else :
    for i in range(0,n,3):
        if i+1 < n :
            res = res +  price[i] + price[i+1]
        elif i <= n-1 :
            res += price[i]
        else :
            break

print(res)
       
        