import itertools
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
res = list(itertools.product(arr,repeat=m))
res = sorted(list(set(res)))

for i in res:
    print(*i)



##############################################
# 백 트래킹
##############################################


n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
res = []


def backTracking() :
    if len(res) == m :
        print(*res)
        return

    flag = 0
    for i in range(n):
        if flag != arr[i] :
            res.append(arr[i])
            flag = arr[i]
            backTracking()
            res.pop()


backTracking()