
dy = [-1,0,1,0]
dx = [0,1,0,-1]

n,m = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
flag = False

def cleaning(arr) :
    global cnt,r,c
    if arr[r][c] == 0 and not visited[r][c] :
        cnt += 1
        visited[r][c] = True
        

def move(arr) :
    global flag,n,m,d,r,c
    check = False

    for i in range(4) :
        ny = r + dy[i]
        nx = c + dx[i]

        if 0 <= ny < n and 0<= nx < m:
            if arr[ny][nx] == 0 and not visited[ny][nx] :
                check = True
                break

    if check :
        if d == 0 :
            d = 3
        else :
            d -= 1

        if arr[r+dy[d]][c+dx[d]] == 0 and not visited[r+dy[d]][c+dx[d]] :
            r += dy[d]
            c += dx[d]

    else :
        ny = r - dy[d]
        nx = c - dx[d]
        if arr[ny][nx] == 0 :
            r = ny
            c = nx
        else :
            flag = True
            return

def check(arr) :
    checking = True
    for a in arr :
        if not all(a) :
            checking = False
            return checking

    return checking

    

while not flag :

    if check(arr) :
        break

    cleaning(arr)
    move(arr)

print(cnt)