import copy
n,m,y,x,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cmds = list(map(int,input().split()))

dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]
#동서북남

# dice 초기화
dice = [[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]

def to_south(dice) :
    tmp = copy.deepcopy(dice)

    for i in range(4):
        dice[i][1] = tmp[(i+1)%4][1]

def to_north(dice) :
    tmp = copy.deepcopy(dice)

    for i in range(4) :
        dice[(i+1)%4][1] = tmp[i][1]

def to_east(dice) :
    tmp = copy.deepcopy(dice) 

    #걍 빡구현 해야지.......
    dice[1][2] = tmp[1][1]
    dice[3][1] = tmp[1][2]
    dice[1][0] = tmp[3][1]
    dice[1][1] = tmp[1][0]


def to_west(dice) :
    tmp = copy.deepcopy(dice) 

    dice[1][2] = tmp[3][1]
    dice[3][1] = tmp[1][0]
    dice[1][0] = tmp[1][1]
    dice[1][1] = tmp[1][2]


# dice[3][1] = value

for c in cmds :
    y += dy[c]
    x += dx[c]

    if y <0 or y >= n or x < 0 or x >= m :
        y -= dy[c]
        x -= dx[c]
        continue

    if c == 1 :
        to_east(dice)
    elif c == 2 :
        to_west(dice)
    elif c == 3 :
        to_north(dice)
    elif c == 4 :
        to_south(dice)

    if arr[y][x] == 0 :
        arr[y][x] = dice[3][1]
    else :
        dice[3][1] = arr[y][x]
        arr[y][x] = 0

    print(dice[1][1])

    