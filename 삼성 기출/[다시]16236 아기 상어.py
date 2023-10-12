from collections import deque

#상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
#입력받기
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
#상어 초기 크기 2, 먹은 고기 0마리
shark = [2,0]
shark_loc = []
#상어 위치 찾기
shark_flag = False

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9 :
            arr[i][j] = 0
            shark_loc = [i,j]
            shark_flag = True
            break
    if shark_flag :
        break


#종료 조건
# def call_mom(arr,shark_size) :
#     #모두 0이거나 상어보다 큰애만 남았거나 = 0이 아니면서 상어보다 작은애가 있거나
#     for a in arr :
#         if any([(x != 0 and x <= shark_size) for x in a]) :
#             return False #더 먹을 고기가 있음 -> 엄마부르기 ㄴ

#     return True #못찾으면 걍 엄마 불러야댐 => 종료 조건


def shark_sizeup(shark) :
    if shark[1] >= shark[0] :
        shark[1] -= shark[0]
        shark[0] += 1

    return shark

def bfs(n,arr,cnt,shark,shark_loc) :
    visited = [[False] * n for _ in range(n)]
    visited[shark_loc[0]][shark_loc[1]] = True
    q = deque([])
    q.append([shark_loc[0],shark_loc[1],cnt]) # 샤크 위치, 이동한 시간
    res = []

    while q :
        y,x,time = q.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n :
                continue
            else :
                if arr[ny][nx] <= shark[0] and not visited[ny][nx] :
                    # 이동 가능
                    if arr[ny][nx] != 0 and arr[ny][nx] < shark[0] :
                        res.append([ny,nx,time+1])
                    q.append([ny,nx,time+1])
                    visited[ny][nx] = True
                    
    res.sort(key=lambda x : [x[2],x[0],x[1]])
    return res 



time = 0
while True :
    res = bfs(n,arr,time,shark,shark_loc)
    if len(res) == 0 :
        print(time)
        break

    y,x,cnt = res[0]
    arr[y][x] = 0
    shark_loc = [y,x]

    shark[1] += 1
    shark_sizeup(shark)
    time = cnt
        
