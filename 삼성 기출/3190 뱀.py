from collections import deque

dir = [[0,1],[1,0],[0,-1],[-1,0]]
# 오 => i+1 % 4, 왼 -> i-1 % 4

n = int(input())
k = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    apple = list(map(int,input().split()))
    board[apple[0]][apple[1]] = 1

l = int(input())
cmd = []
cmd_index = 0
for _ in range(l) :
    x,y = list(input().split())
    cmd.append([int(x),y])


def turn_right(d) :
    d = (d+1) % 4
    return d

def turn_left(d) :
    if d == 0 :
        d = 3
    else :
        d -= 1

    return d

def play(cmd,cmd_idx) :
    cnt = 0
    d = 0
    visited = [[False] * (n+1) for _ in range(n+1)]
    q = deque([])
    q.append([1,1])
    visited[1][1] = True

    while q :
        y,x = q[len(q)-1]
        cnt += 1
        ny = y + dir[d][0]
        nx = x + dir[d][1]

        if ny <= 0 or ny > n or nx <= 0 or nx > n or visited[ny][nx] :
            print(cnt)
            return

        elif board[ny][nx] == 1 :
            board[ny][nx] = 0
            q.append([ny,nx])

        else :
            q.append([ny,nx])
            v_y,v_x = q.popleft()
            visited[v_y][v_x] = False
        visited[ny][nx] = True

        if cmd_idx >= len(cmd) :
            continue
        else :
            if cmd[cmd_idx][0] == cnt :
                if cmd[cmd_idx][1] == 'D' :
                    d = turn_right(d)
                else :
                    d = turn_left(d)

                cmd_idx += 1

play(cmd,cmd_index)
            