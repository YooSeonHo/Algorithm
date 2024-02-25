from collections import deque

n = int(input())
k = int(input())
arr = list(map(int,input().split()))

# q = num, time, recomand # 
q = deque([])
idx = 0

while True :
    if len(q) == n :
        break

    q.append([arr[idx],idx+1,1])
    idx += 1

for i in range(idx,k) :
    q.sort(key = lambda x : (-x[2],x[1]))