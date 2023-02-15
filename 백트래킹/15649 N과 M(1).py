import itertools

n,m = map(int,input().split())

arr = [i for i in range(1,n+1)]
res = list(itertools.permutations(arr,m))

for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j], end=' ')
    print()