n,m = map(int,input().split())
arr = []

def dfs(idx):
    if len(arr) == m :
        print(' '.join(map(str,arr)))
        return
    else :
        for i in range(idx,n+1):
            arr.append(i)
            dfs(i)
            arr.pop()

dfs(1)

####################################
import itertools
n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
res = list(itertools.combinations_with_replacement(arr,m))

for i in res :
    print(*i,sep=' ')
        