import itertools

n,m = map(int,input().split())
arr = list(map(int,input().split()))

res = list(itertools.permutations(arr,m))
res.sort()

for i in res:
    print(*i, sep=' ')

###############################################

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
res = []

def dfs() :
    if len(res) == m :
        print(' '.join(map(str,res)))
        return
    else :
        for i in arr :
            if i not in res :
                res.append(i)
                dfs()
                res.pop()
dfs()