import sys
from collections import deque
imput = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m,k = list(map(int,imput().split()))
arr = [list(imput().rstrip()) for _ in range(n)]
voca = imput().rstrip()
q = deque([])
cnt = 0

for i in range(n) :
    for j in range(m) :
        if arr[i][j]==voca[0] :
            q.append((voca[0],(i,j)))

while q:
    x,path = q.popleft()

    if x == voca:
        cnt +=1
        continue

    for i in range(1,k+1):
        for j in range(4):
            nx = path[1] + dx[j] * i
            ny = path[0]+ dy[j] * i
            if 0<=nx<m and 0<=ny<n :
                if arr[ny][nx] == voca[len(x)] :
                    q.append((x + voca[len(x)],(ny,nx)))    


print(cnt)