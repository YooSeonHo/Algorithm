from collections import defaultdict


dx = [0,-1,1,1,0,1,1,1]
#col
dy = [-1,-1,0,1,1,1,0,-1]
#row
s_dx = [-1,0,1,0]
s_dy = [0,-1,0,1]


m,s = map(int,input().split())
fishes = defaultdict(list)
smells = defaultdict(list)
for _ in range(m) :
    x,y,d = list(map(int,input().split()))
    fishes[(x,y)].append(d)

shark = list(map(int,input().split()))
board = [[0] * 5 for _ in range(5)]

# 입력 부분

def fish_move(board,shark,x,y,d) :

    for i in range(8) :
        nx = x + dx[(d+i) % 8]
        ny = y + dy[(d+i) % 8]

        if shark[0] == nx and shark[1] == ny :
            continue

        if nx <= 0 or nx > 5 or ny <= 0 or ny > 5 :
            continue

        if ((nx,ny) in smells) :
            continue
    
        board[nx][ny] += 1
        break


