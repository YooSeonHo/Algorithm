import sys
imput = sys.stdin.readline

r,c = map(int,imput().split())
arr = []
for i in range(r):
    arr.append(list(map(int,imput().split())))

res = []

for i in range(r):
    res.append(min(arr[i]))

print(max(res))