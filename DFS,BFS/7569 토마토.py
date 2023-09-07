from collections import deque
m,n,height = list(map(int,input().split()))
# m = 가로, n = 세로 , h = 높이

graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(height)]
visited = [[[False] * m for _ in range(n)] for _ in range(height)]

dy = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]

flag = False

q = deque([])

def makeQ():
    # 모두 익어있는 상태인지 체크
    for x in range(height):
        for y in range(n):
            for z in range(m):
                if graph[x][y][z] == 1 :
                    q.append([x,y,z,0])
                    visited[x][y][z] = True
                elif graph[x][y][z] == -1 :
                    visited[x][y][z] = True

def check(arr) :
    for x in range(height):
        for y in range(n):
            for z in range(m):
                if arr[x][y][z] == 0 :
                    return False

    return True

def bfs():
    makeQ()
    while q :
        h,y,x,days = q.popleft()

        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nh < 0 or nh >= height or ny < 0 or ny >= n or nx < 0 or nx >= m :
                continue
            else :
                if not visited[nh][ny][nx] :
                    if graph[nh][ny][nx] == -1 :
                        continue
                    elif graph[nh][ny][nx] == 0 :
                        q.append([nh,ny,nx,days+1])
                        visited[nh][ny][nx] = True
                        graph[nh][ny][nx] = days+1
                    else :
                        visited[nh][ny][nx] = True




if check(graph) :
    # 토마토 박스에 0이 없으면 모두 익어있는거
    print(0)
else :
    bfs()
    if not check(visited) :
        print(-1)
    else :
        maxNum = 0
        for x in range(height):
            for y in range(n):
                for z in range(m):
                    if graph[x][y][z] > maxNum :
                        maxNum = graph[x][y][z]
                    else :
                        continue


        print(maxNum)