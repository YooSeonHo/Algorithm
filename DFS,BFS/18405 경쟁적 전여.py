import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
s,x,y = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs():
    ##q에 (바이러스번호,x,y,sec)순으로 입력
    q = deque([])
    temp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 :
                temp.append((arr[i][j],i,j,0))

    temp.sort(key = lambda x : x[0])
    
    for i in temp :
        q.append(i)

    while q:
        vir,x,y,sec = q.popleft()
        if sec == s :
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n :
                if arr[nx][ny] == 0 :
                    arr[nx][ny] = vir
                    q.append((vir,nx,ny,sec+1))

bfs()
print(arr[x-1][y-1])