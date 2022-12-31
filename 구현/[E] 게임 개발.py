import sys
imput = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int,imput().split())
row,col,dir = map(int,imput().split())
arr = [list(map(int,imput().split())) for _ in range(n)]
# 2차원 배열 입력받기

cnt = 1
arr[row][col] = 1

while True :
    for i in range(4):
        nx = row + dx[dir % 4]
        ny = col + dy[dir % 4]

        if arr[nx][ny] == 1 or nx < 0 or ny < 0 or nx > m or ny > n :
            dir += 1
            continue
        else :
            cnt += 1
            arr[nx][ny] = 1
            dir = dir%4
            row = nx
            col = ny
            break
    if dir >= 4:
        break

print(cnt)
        
