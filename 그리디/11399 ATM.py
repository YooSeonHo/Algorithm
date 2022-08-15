import sys
imput = sys.stdin.readline

n = int(imput())
time = list(map(int,imput().split()))

time.sort()
res = 0

for i in range(n):
    res += (time[i] * (n-i))

print(res) 