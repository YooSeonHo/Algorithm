import sys
imput = sys.stdin.readline

n,m = map(int,imput().split())
a = list(map(int,imput().split()))
b = list(map(int,imput().split()))

res = a+b
res.sort()

for i in res:
    print(i,end=' ')