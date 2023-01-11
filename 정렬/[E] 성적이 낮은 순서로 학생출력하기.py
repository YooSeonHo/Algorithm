n = int(input())
arr = []

for _ in range(n):
    tmp = input().split()
    arr.append((tmp[0],int(tmp[1])))

arr.sort(key = lambda x : x[1])

for i in range(n):
    print(arr[i][0], end=' ')