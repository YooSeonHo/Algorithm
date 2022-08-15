import sys
n,k = map(int,input().split())
coins  = []

for i in range(n):
    coins.append(int(input()))

cnt = 0

coins.sort(reverse=True)

for i in coins:
    if i > k :
        continue
    else:
        cnt += k//i
        k = k%i

print(cnt)