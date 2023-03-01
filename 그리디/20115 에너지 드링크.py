import sys
input = sys.stdin.readline

n = int(input())
drink = list(map(int,input().split()))
drink.sort()

res = drink[n-1]
for i in range(n-1):
    res = res + drink[i]/2

print(res)