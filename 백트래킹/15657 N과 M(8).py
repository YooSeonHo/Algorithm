import itertools


n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

res = list(itertools.combinations_with_replacement(arr,m))

for r in res :
    print(*r)


##########################################################
#백 트래킹으로 풀어보장


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
            if max(res) <= i :
                backTracking()
            res.pop()
            continue

backTracking()

