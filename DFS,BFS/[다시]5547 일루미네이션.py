from collections import deque

w,h = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(h)]
home = [[0] * (w+2) for _ in range(h+2)]
visited = [[0] * (w+2) for _ in range(h+2)]

for i in range(h):
    for j in range(w):
        home[i+1][j+1] = graph[i][j]
        # 겉에 외벽을 쌓아서 가장자리 까지 count할 수 있어짐

odd_dy = [1,-1,0,0,1,-1]
odd_dx = [0,0,1,-1,1,1]

even_dy = [1,-1,0,0,-1,1]
even_dx = [0,0,1,-1,-1,-1]

cnt = 0

q = deque([[0,0]])
visited[0][0] = True

while q:
    y,x = q.popleft()

    if y % 2 == 0 :
        for i in range(6):
            ny = y + even_dy[i]
            nx = x + even_dx[i]

            if ny < 0 or ny >= (h+2) or nx < 0 or nx >= (w+2):
                continue
            else :
                #0 인애를 큐에 넣고, 6방향이 1이면 cnt + 1, 0이면 또 큐에 넣는다
                if home[ny][nx] == 1 :
                    cnt += 1
                elif home[ny][nx] == 0 :
                    if not visited[ny][nx] :
                        q.append([ny,nx])
                        visited[ny][nx] = True
                        
    else :
        for i in range(6):
            ny = y + odd_dy[i]
            nx = x + odd_dx[i]

            if ny < 0 or ny >= (h+2) or nx < 0 or nx >= (w+2):
                continue
            else :
                #0 인애를 큐에 넣고, 6방향이 1이면 cnt + 1, 0이면 또 큐에 넣는다
                if home[ny][nx] == 1 :
                    cnt += 1
                elif home[ny][nx] == 0 :
                    if not visited[ny][nx] :
                        q.append([ny,nx])
                        visited[ny][nx] = True



print(cnt)
                


