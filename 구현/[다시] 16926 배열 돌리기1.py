import sys
input =  sys.stdin.readline


# n * m , r번 로테이트
n,m,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]


for _ in range(r):

    for i in range(min(n,m) // 2):
        x,y = i , i
        temp = arr[y][x]

        #하
        for j in range(i+1,n-i):
            y = j
            prev = arr[y][x]
            arr[y][x] = temp
            temp = prev

        #우
        for j in range(i+1,m-i):
            x = j
            prev = arr[y][x]
            arr[y][x] = temp
            temp = prev
        #상
        for j in range(i+1,n-i):
            y = n - j - 1
            prev = arr[y][x]
            arr[y][x] = temp
            temp = prev

            
        #좌
        for j in range(i+1,m-i) : 
            x = m -  j -  1
            prev = arr[y][x]
            arr[y][x] = temp
            temp = prev

for a in arr :
    print(*a)

      

# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m,r = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(n)]
# q = deque([])
# for i in range(min(n,m)//2) :
#     q.clear()
#     q.extend(arr[i][i:m-i])
#     q.extend(arr[i+1:n-1-i][m-i-1])
#     q.extend(arr[n-i-1][i:m-i][::-1])
#     q.extend(arr[n-i-1][n-i-2:i+1:-1])

#     q.rotate(-r)
#     print(q)