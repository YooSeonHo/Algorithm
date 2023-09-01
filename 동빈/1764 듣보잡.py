import sys
input = sys.stdin.readline

n,m = map(int,input().split())
listen = []
look = []

for i in range(n):
    listen.append(input().strip())

for i in range(m):
    look.append(input().strip())

res = list(set(listen) & set(look))
res.sort()
print(len(res))
print(*res,sep='\n')