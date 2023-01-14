n = int(input())
arr = list(map(int,input().split()))

res = [0] * n
res[0] = arr[0]
res[1] = max(arr[0],arr[1])
for i in range(2,n):
    res[i] = max(res[i-2]+arr[i],res[i-1])

print(res[n-1])