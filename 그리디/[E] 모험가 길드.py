n = int(input())
arr = list(map(int,input().split()))

res = 0
arr.sort()

cnt = 0

for i in arr :
    cnt +=1
    if cnt >= i :
        res +=1
        cnt = 0

print(res)