import itertools

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

res = list(itertools.combinations(arr,m))

for i in res :
    print(*i, sep=' ')

##############################################
#백트래킹으로 풀어보기


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
            if i not in res :
                res.append(i)
                if max(res) == i :
                    backTracking()
                res.pop()


backTracking()

##########################################################

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()

res = []

def backTracking(start) :
    if len(res) == m :
        print(*res)
        return

    else :
        for i in range(start,len(arr)) :
            if arr[i] not in res :
                res.append(arr[i])
                backTracking(i + 1)
                ## start가 아니라 i 를 넣어줘야한덩..
                res.pop()


backTracking(0)