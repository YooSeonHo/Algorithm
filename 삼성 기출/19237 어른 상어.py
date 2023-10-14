from collections import defaultdict

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
shark_dir = [0] + list(map(int,input().split()))
# 현재 i번 상어가 바라보는 방향!!!! => 방향이 바뀔 떄 마다 갱신해줘야함  1,2,3,4 => 상 하 좌 우
shark = [[-1] for _ in range(m+1)]
shark_priority = defaultdict(list)

dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]
time = 0
for i in range(1,m+1) :
    for _ in range(4) :
        shark_priority[i].append(list(map(int,input().split())))

####################입력#########################################

game = [[defaultdict(int) for _ in range(n)] for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 0 :
            continue
        else :
            num = board[i][j]
            shark[num] = [i,j,shark_dir[num]]
            game[i][j][num] = k
# 상어 초기화 => 1부터 시작, y, x, dir 순으로 저장

#게임판 만들기 => i번 상어 k초
# 모든 상어 이동 함수 만들기
def move_shark(game_original) :
    #1. 인접 칸 중 냄새가 없는 칸 2. 자신의 냄새가 있는 칸 순서로 탐색, 선택지가 많을 경우 우선순위에 따라서
    # 순차적으로 이동 -> 같은 시간이더라도 먼저 간애가 자리 잡으면 두번쨰 간애는 해당 칸으로 못가게 되어버린다
    global k
    tmp = []
    for i in range(1,m+1) :
        if shark[i] == - 1 :
            continue
        y,x,dir = shark[i]
        flag = False
        game = [dim[:] for dim in game_original]
        for j in range(4) :
            direction = shark_priority[i][dir-1][j]

            ny = y + dy[direction]
            nx = x + dx[direction]

            if 0 <= ny < n and 0 <= nx < n :
                # 냄새 길이가 0이거나 , 모든 벨류가 0이면 냄새가 없는거
                if len(game[ny][nx]) == 0 or all([0 == x for x in game[ny][nx].values()]) :
                    #상어가 그 자리로 이동
                    shark[i] = [ny,nx,direction]
                    #해당 자리에 냄새 묻히기
                    tmp.append([ny,nx,i])
                    flag = True
                    break
            
        if flag :
            continue
        else :
            for j in range(4) :
                direction = shark_priority[i][dir-1][j]

                ny = y + dy[direction]
                nx = x + dx[direction]

                if 0 <= ny < n and 0 <= nx < n :
                    if len(game[ny][nx]) == 0 :
                        continue 
                    else :
                        if game[ny][nx][i] > 0 :
                            #1씩 감소시킬거라서 0이 남아있을 수도 있음...
                            shark[i] = [ny,nx,direction]
                            tmp.append([ny,nx,i])
                            break

    #모든 상어 이동이 끝난거!
    for s in tmp :
        game[s[0]][s[1]][s[2]] = k+1

#상어 쫓아내기 함수
def exit_shark() :
    #같은 칸에 있는 상어 중 크기가 큰애를 쫓아내면 댐
    for i in range(1,m+1) :
        if shark[i] == -1 :
            continue
        for j in range(i+1,m+1) :
            if shark[j] == -1 :
                continue
            if [shark[i][0],shark[i][1]] == [shark[j][0],shark[j][1]] :
                shark[j] = -1 
                # 쫓아내깅...

#냄새 없애기 함수
def decrease_smell() :
    for i in range(n):
        for j in range(n) :
            if len(game[i][j]) == 0 :
                continue
            else :
                for s in game[i][j].keys() :
                    if game[i][j][s] > 0 :
                        game[i][j][s] -= 1


def shark_check() :
    for i in range(2,m+1) :
        if shark[i] != -1 :
            return True

    return False 


while True :

    if time >1000 :
        print(-1)
        break

    if shark_check() :
        time += 1
        move_shark(game)
        decrease_smell()
        exit_shark()
    else :
        print(time)
        break

# 저장을 어떻게 할까? 2차원 배열? 딕셔너리? 
# 상어 별 위치, 방향, 냄새 저장소 저장?
# 구간 별 냄새 저장, 2차원 배열 속 냄새 딕셔너리 저장?
# 2차원 배열을 만들고 각 요소가 딕셔너리야, 거기에 상어 번호랑 시간을 기록하고, 시간이 지날때마다 모든 배열을 돌면서 -1
# 상어는 어케 저장? => 초기화 때 2중 포문으로 다 돌아서 찾고, 방향이랑 같이 기록

# 초기 상어 위치를 찾아서 미리 저장? 해야하나?
# 냄새를 뿌리고 끝 => 이게 초기화?

# 이동할 방향을 찾아서 움직여, 냄새를 1씩 지워
# 냄새를 뿌려
# 겹쳐있는 상어를 잡아 -> 번호가 큰애가 잡힐 땐 냄새를 남기지 않고 바로 사망
# 반복