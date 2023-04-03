import sys
input = sys.stdin.readline

def rotate(arr,dir) :
    tmp = [[] for _ in range(4)]
    for i in range(len(arr)):
        tmp[0].append(arr[i][i])
        tmp[1].append(arr[i][len(arr)//2])
        tmp[2].append(arr[i][len(arr)-i-1])
        tmp[3].append(arr[len(arr)//2][i])

    if dir == 1:
        for i in range(len(arr)):
            arr[i][len(arr)//2] = tmp[0][i]
            arr[i][len(arr)-i-1] = tmp[1][i]
            arr[len(arr)//2][i] = tmp[2][len(arr)-1-i]
            arr[i][i] = tmp[3][i]
    else : 
        for i in range(len(arr)):
            arr[len(arr)//2][i] = tmp[0][i]
            arr[i][i] = tmp[1][i]
            arr[i][len(arr)//2] = tmp[2][i]
            arr[len(arr)-i-1][i] = tmp[3][i]

    
    


t = int(input())
for _ in range(t):
    n,d = map(int,input().split())

    if n == 1:
        print(int(input()))
    else :
        arr = [list(map(int,input().split())) for _ in range(n)]

        cnt = d // 45

        if cnt >=0 : 
            for _ in range(cnt):
                rotate(arr,1)
        else :
            for _ in range(-cnt):
                rotate(arr,-1)

        for i in arr :
            print(*i,sep=' ')

            