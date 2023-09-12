import itertools
import sys
sys.setrecursionlimit(10**6)

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
res = []
per = list(itertools.permutations(arr,m))
res = list(set(per))
res.sort()


for p in res :
    flag = False
    for i in range(1,len(p)):
        if p[i-1] > p[i] :
            flag = True
            break
        else :
            continue

    if flag :
        continue
    else :
        print(*p)


########################################################
# 백트래킹으로 풀어보자

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
res = []
visited = [0] * n

def backTracking(start) :
    if len(res) == m :
        print(*res)
        return

    flag = 0
    for i in range(start,n) :
        if not visited[i] and flag != arr[i] :          
            res.append(arr[i])
            flag = arr[i]
            visited[i] = True
            backTracking(i+1)
            visited[i] = False
            res.pop()

backTracking(0)