n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
res = []


def backTracking(start) :
    if len(res) == m :
        print(*res)
        return

    flag = 0
    for i in range(start,n):
        if flag != arr[i] :
            res.append(arr[i])
            flag = arr[i]
            backTracking(i)
            res.pop()


backTracking(0)