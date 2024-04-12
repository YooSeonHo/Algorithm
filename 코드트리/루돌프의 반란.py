import sys
from heapq import heappush,heappop
from collections import defaultdict
input = sys.stdin.readline

n,m,p,c,d = map(int,input().split())
cow = list(map(int,input().split()))
santa = [[] for _ in range(p+1)]
score = [0] * (p+1)
stun = defaultdict(int)
flag = False

for _ in range(p) :
    x,y,z = map(int,input().split())
    santa[x] = [y,z]

def calc_distance(r1,c1,r2,c2) :
    res = (r1 - r2) ** 2 + (c1 - c2) ** 2
    return res

def move_cow() :
    global flag
    dy = [1,1,1,0,0,-1,-1,-1]
    dx = [-1,0,1,1,-1,1,0,-1]

    q = []
    
    for i in range(1,p+1) :
        if santa[i] :
            a,b = santa[i]
            # 대각선 2 = 직선 1임... => 대각선인지 판별... ㅠ
            # if abs(cow[0]-a) == abs(cow[1]-b) :
            #     dist = abs(cow[0]-a) ** 2
            # else :
            dist = calc_distance(cow[0],cow[1],a,b)
            heappush(q,(dist,-a,-b,i))
    if q :
        target = heappop(q)
    else :
        flag = True
        return
    tmp = []
    # 이동 방향 정하기
    for i in range(8) :
        ny = cow[0] + dy[i]
        nx = cow[1] + dx[i]

        if 1 <= ny <= n and 1 <= nx <= n :
            check = calc_distance(ny,nx,-target[1],-target[2])
            if not tmp :
                tmp = [check,i]
            else :
                if tmp[0] > check :
                    tmp = [check,i]

    return [dy[tmp[1]],dx[tmp[1]]]
    # 루돌프 이동 방향 리턴

def interaction(num,y,x,dy,dx) :
    for i in range(1,p+1) :
        if not santa[i] :
            continue
        if i == num :
            continue

        if santa[i] == [y,x] :
            santa[i] = [santa[i][0] + dy, santa[i][1]+dx]
            if not (1 <= santa[i][0] <= n and 1 <= santa[i][1] <= n) :
                santa[i] = 0
                return
            interaction(i,santa[i][0],santa[i][1],dy,dx)
            break

def check_meet(cow,num,point,how) :
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    if cow == santa[num] and santa[num] :
        score[num] += point
        if how == -1 :
            santa[num][0] += cow_dir[0] * point
            santa[num][1] += cow_dir[1] * point
        else :
            santa[num][0] -= dy[how] * point
            santa[num][1] -= dx[how] * point

        if not (1 <= santa[num][0] <= n and 1 <= santa[num][1] <= n) :
            santa[num] = 0
            return True

        # 상호작용 체크 해야댐
        if how == -1 :
            interaction(num,santa[num][0],santa[num][1],cow_dir[0],cow_dir[1])
        else :
            interaction(num,santa[num][0],santa[num][1],-dy[how],-dx[how])
        return True
    return False

def move_santa(num) :
    q = []    
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    now = calc_distance(santa[num][0],santa[num][1],cow[0],cow[1])

    for i in range(4) :
        ny = santa[num][0] + dy[i]
        nx = santa[num][1] + dx[i]
        if 1 <= ny <= n and 1 <= nx <= n and [ny,nx] not in santa :
            heappush(q,(calc_distance(ny,nx,cow[0],cow[1]),i))

    if q :
        move = heappop(q)
        if now > move[0] :
            santa[num] = [santa[num][0] + dy[move[1]],santa[num][1] + dx[move[1]]]

    #충돌 체크
        if check_meet(cow,num,d,move[1]) :
            stun[num] = 2

for _ in range(m) :
    #루돌프 이동
    cow_dir = move_cow()
    if flag :
        break
    cow = [cow[0]+cow_dir[0], cow[1]+cow_dir[1]]

    #여기서 충돌 체크 
    for i in range(1,p+1) :
        if check_meet(cow,i,c,-1) :
            stun[i] = 2
            break

    #산타 1~p 이동
    for i in range(1,p+1) :
        if not santa[i] or stun[i] :
            continue
        else :
            move_santa(i)

    for i in range(1,p+1) :
        if santa[i] :
            score[i] += 1
        if stun[i] :
            stun[i] -= 1

    # print(cow)
    # print(santa[1:])
    # print(score)
print(*score[1:])