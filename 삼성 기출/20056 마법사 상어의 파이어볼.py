
n,m,k = list(map(int,input().split()))
fireball = [list(map(int,input().split())) for _ in range(m)]
# 입력 받기 r,c,m(질량) ,s(속력) ,d(방향) 순서

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

board = [[[] for _ in range(n)] for _ in range(n)]

for f in fireball :
    board[f[0]-1][f[1]-1].append([f[0]-1,f[1]-1,f[2],f[3],f[4]])
# 보드판 초기화 완료

def move_ball() :
    global n
    #모든 볼 이동 => 이미 한번 이동한 애까지 이동되어 버림 ?
    tmp_board = [[[] for _ in range(n)] for _ in range(n)]
    #굳이 tmp를 두지 않고, q를 만들어서 이동시킬 애들을 다 넣어둔 후 이동 시켜도 되겠네
    for i in range(n) :
        for j in range(n) :
            if len(board[i][j]) == 0 :
                continue
            else :
                for b in board[i][j] :
                    y,x,mass,speed,dir = b
                    ny = (y + (dy[dir] * speed)) % n
                    nx = (x + (dx[dir] * speed)) % n

                    tmp_board[ny][nx].append([ny,nx,mass,speed,dir])
    # 이동한 거 또 이동 시키는 거 방지하려고 tmp 만든건데 무용지물... => 심지어 내 칸으로 이동 시킨애를 지워버리기 까지함!!!!!


    #같은 칸에 있는 볼 체크
    for i in range(n) :
        for j in range(n) :
            if len(tmp_board[i][j]) < 2 :
                continue
            else :
                # r = i , c = j
                tmp_m = 0
                tmp_s = 0
                odd_flag = False
                even_flag = False
                for b in tmp_board[i][j] :
                    tmp_m += b[2]
                    tmp_s += b[3]
                    if b[4] % 2 == 0 :
                        even_flag = True
                    else :
                        odd_flag = True

                res_m = tmp_m // 5
                res_s = tmp_s // len(tmp_board[i][j])
                tmp_board[i][j] = []

                if res_m == 0 :
                    #나눴을 때 질량이 0? 걍 다 소멸
                    continue
                else :
                    if even_flag and odd_flag :
                        for it in range(1,8,2) :
                            tmp_board[i][j].append([i,j,res_m,res_s,it])

                    else :
                        for it in range(0,7,2) :
                            tmp_board[i][j].append([i, j, res_m, res_s, it])

    return tmp_board

def check_ball() :
    global n
    res = 0
    for i in range(n) :
        for j in range(n) :
            if len(board[i][j]) == 0 :
                continue
            else :
                for b in board[i][j] :
                    res += b[2]

    return res


for _ in range(k) :
    board = move_ball()
print(check_ball())
