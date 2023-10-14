import copy
#↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

#입력 받기
arr = [list(map(int,input().split())) for _ in range(4)]
fish = [[0] * 4 for _ in range(4)]
# visited = [[False] * 4 for _ in range(4)]

for i in range(4) :
    for j in range(4) :
        #01, 23, 45,

        fish[i][j] = [arr[i][2*j], arr[i][2*j+1]]

shark = [0,0,fish[0][0][0],fish[0][0][1]]
# 상어 y ,x , 크기, 방향 순서
res = shark[2]
fish[0][0] = []
# visited[0][0] = True
#초기화 끝!
def fish_move(fish,shark) :
    #1번 물고기부터 차례로 이동 시작할거
    for num in range(1,17) :
        flag = False
        for i in range(4) :
            for j in range(4) :
                if len(fish[i][j]) == 0 :
                    continue

                size,dir = fish[i][j][0], fish[i][j][1]

                if size != num :
                    continue
                
                for k in range(8) :
                    ny = i + dy[(dir+k-1)%8]
                    nx = j + dx[(dir+k-1)%8]

                    if 0<= ny < 4 and 0 <= nx < 4 and [shark[0],shark[1]] != [ny,nx]:
                        #이동 가능
                        fish[i][j][1] = (dir+k)%8
                        #내 방향을 바꿔놓고 그 다음에 물고기 위치 변경 진행
                        tmp = fish[ny][nx]
                        fish[ny][nx] = fish[i][j]
                        fish[i][j] = tmp
                        # fish[i][j],fish[ny][nx] = fish[ny][nx],fish[i][j]
                        # visited[ny][nx],visited[i][j] = visited[i][j], visited[ny][nx]
                        flag = True
                        break
                if flag :
                    break
            if flag :
                break

    

def end_shark(y,x,dir,fish) :
    flag = False
    for i in range(1,4) :
        ny = y + dy[(dir-1)%8] * i
        nx = x + dx[(dir-1)%8] * i
        #만약에 갈 수 있는 곳이 한 곳이라도 있으면 False 반환!
        if 0 <= ny < 4 and 0 <= nx < 4 and len(fish[ny][nx]) != 0 :
            flag = True
    if flag :
        return False
    else :
        return True


def bfs(fish,shark) :
    global res

    # 그러니까 백 트래킹이 끝나면 내가 바꿨던 fish, shark 다 백트래킹 전으로 돌려야하는데 그 부분이 빠쪄있음!
    shark_y,shark_x,shark_size,shark_dir = shark
    fish_move(fish,shark)


    if end_shark(shark[0],shark[1],shark[3],fish) :
        res = max(res,shark[2])
        return

    for i in range(1,4) :
        
        ny = shark[0] + dy[(shark[3]-1)%8] * i
        nx = shark[1] + dx[(shark[3]-1)%8] * i

        # if 0<=ny<4 and 0<=nx<4 and not visited[ny][nx] :
        if 0<=ny<4 and 0<=nx<4 and not len(fish[ny][nx]) == 0 :
            shark = [ny,nx,shark[2]+fish[ny][nx][0],fish[ny][nx][1]]
            tmp = fish[ny][nx]
            fish[ny][nx] = []
            # visited[ny][nx] = True
            bfs(copy.deepcopy(fish),shark)
            # bfs 끝나고 나왔는데도 물고기가 이미 한번 움직인 상태.........
            shark = [shark_y,shark_x,shark_size,shark_dir]
            # visited[ny][nx] = False
            fish[ny][nx] = tmp


bfs(copy.deepcopy(fish),shark)
print(res)

