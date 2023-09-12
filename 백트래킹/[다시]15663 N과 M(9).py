import itertools


n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
res = []
visited = [0] * n

#인덱스로 띠져보자

def backTracking() :
    if len(res) == m:
        print(*res)
        return

    # 19 19 두번이 나오거나 99 가 안나오거나 둘중 하나밖에 못만드는데? => flag를 만들어서 체크
    flag = 0
    for i in range(n):
        if not visited[i] and flag != arr[i] :
            res.append(arr[i])
            visited[i] = True
            flag = arr[i]
            backTracking()
            visited[i] = False
            res.pop()


        


backTracking()