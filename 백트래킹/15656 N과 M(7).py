import itertools


n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

res = list(itertools.product(arr,repeat=m))

for r in res :
    print(*r)


###################################################33
#백트래킹
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

res = []

def backTracking() :
    if len(res) == m :
        print(*res)
        return
    else :
        for i in arr :
            res.append(i)
            backTracking()
            res.pop()

backTracking()