n = int(input())
check = int(input())
num = n**2
board = [[0] * n for _ in range(n)] 
## D R U L
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = 0
x,y = 0,0
ansX , ansY = 0,0

while num > 0:
    board[y][x] = num
    nx = x + dx[dir]
    ny = y + dy[dir]
    if num == check :
        ansX = x+1
        ansY = y+1
    
    if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] != 0 :
        dir = (dir+1) %4
    
    y += dy[dir]
    x += dx[dir]
    num -=1
    









for i in board :
    print(*i)

print(ansY, ansX)