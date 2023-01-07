import sys
imput = sys.stdin.readline

n,m = map(int,imput().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#띄어쓰기 없는 2차원 배열 입력받기
""" 
arr = [list(map(int,imput().split())) for _ in range(n)]
라인으로 입력받은 후에 int로 바꾸는 게 아니라 한글자씩 int로 바꿔서 list에 넣어야함 ....... 
"""

arr = [list(map(int,input())) for _ in range(n)]
#걍 이런식으로 하면 알아서 띄어쓰기 없는 입력도 2차원 배열 생성 가능

visited = [[False] * m for _ in range(n)]
global cnt
cnt = 0

global flag 
flag = False
def dfs(arr,x,y,visited):
    global flag
    global cnt

    if not flag:
        flag = True
        cnt +=1

    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <0 or ny <0 or nx >= n or ny>= m:
            continue
        else:
            if not visited[nx][ny] and not arr[nx][ny]: 
                dfs(arr,nx,ny,visited)
                

for i in range(n):
    for j in range(m):
        if not arr[i][j] and not visited[i][j]:
            flag = False
            dfs(arr,i,j,visited)


print(cnt)
#처음 dfs가 불렸을 때만 cnt++되게 어떻게 할까?
    