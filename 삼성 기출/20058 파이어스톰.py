

n,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
l = list(map(int,input().split()))

def rotate(l) : 
    b = 2 ** l
    for y in range(2 ** n // b) : 
        for x in range(2**n // b) :
            tmp = []
            for i in range(b) :
                cols = []
                for j in range(b) :
                    cols.append(board[b * y + i][b * x + j])
                tmp.append(cols)
            
            tmp = list(zip(*tmp[::-1]))
            for i in range(b) :
                for j in range(b) :
                    board[b * y + i][b * x + j] = tmp[i][j]

# 배열을 쪼개서 로테이트하고 다시 합쳐놔야하는데, 어떻게 쪼개고 어떻게 합치지?
