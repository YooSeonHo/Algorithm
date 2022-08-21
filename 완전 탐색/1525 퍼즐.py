from collections import deque
ans = [[1,2,3],[4,5,6],[7,8,0]]

puz = [list(map(int,input().split())) for _ in range(3)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def puzzle():
    q = deque([])
    count = 0
    q.append((puz,count))

    while q:
        print(q)
        x,cnt = q.popleft()
        if x == ans:
            print(cnt)
            return
        else:
            zero = [(i,j) for i in range(3) for j in range(3) if x[i][j]==0]
            for i in range(4):
                nx = zero[0][1] + dx[i]
                ny = zero[0][0] + dy[i]

                if 0<=nx<=2 and 0<=ny<=2:
                    tmp = x
                    tmp[zero[0][1]][zero[0][0]],tmp[ny][nx] = tmp[ny][nx],tmp[zero[0][1]][zero[0][0]]
                    cnt1 = cnt+1
                    q.append((tmp,cnt1))





    print(-1)

puzzle()

