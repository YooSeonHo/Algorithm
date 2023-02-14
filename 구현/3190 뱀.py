# # dir = ['R','D','L','U']
# # [0,1] , [1,0] , [0,-1] , [-1,0] 순
# #오른쪽으로 이동 -> (인덱스+1)%4 , 왼쪽으로 이동 -> (인덱스-1)%4
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# dir = 0
# n = int(input())
# k = int(input())

# game = [[0] * (n+1) for _ in range(n+1)]
# game[1][1] = 1
# snake = [[1,1]]
# apple = [[0] * (n+1) for _ in range(n+1)]

# for _ in range(k):
#     a,b = map(int,input().split())
#     apple[a][b] = 1

# l = int(input())
# change = []

# for _ in range(l):
#     a,b = input().split()
#     change.append((int(a),b))

# sec = 0
# seccnt = 0

# while True :
#     nx = snake[0][0] + dx[dir]
#     ny = snake[0][1] + dy[dir]
#     #머리 부분

#     if (nx <1 or nx > n or ny <1 or ny > n) :
#         sec +=1
#         break
#     elif game[nx][ny] == 1 :
#         sec += 1
#         break

#     print(snake)
#     for i in range(len(snake)):
#         game[snake[i][0] + dx[dir]][snake[i][1] + dy[dir]] =1

#     if apple[nx][ny] != 1:
#         game[snake[len(snake)-1][0]][snake[len(snake)-1][1]] = 0
#     else :
#         snake.append([snake[len(snake)-1][0],snake[len(snake)-1][1]])
#         #꼬리는 어케 이동시킴?
#     for i in range(len(snake)):
#         snake[i][0] = snake[i][0] + dx[dir]
#         snake[i][1] = snake[i][1] + dy[dir]
#     sec += 1

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(game[i][j], end =' ')
#         print()
#     print()

#     #회전을 먼저 이동 후에 해야할듯? 아니지 회전하고 이동해야되나
#     if sec == change[seccnt][0]:
#         if change[seccnt][1] == 'D' :
#             dir = (dir+1) % 4
#         elif change[seccnt][1] =='L':
#             if dir != 0 :
#                 dir -=1
#             else :
#                 dir = 3

#         seccnt += 1


# print(sec)

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = 0
n = int(input())
k = int(input())

game = [[0] * (n+1) for _ in range(n+1)]
game[1][1] = 1
q = deque([])
q.append([1,1])
apple = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    apple[a][b] = 1

l = int(input())
change = []

for _ in range(l):
    a,b = input().split()
    change.append((int(a),b))

sec = 0
secCnt = 0

while q :
    print(q)
    x,y = q.popleft()

    nx = x + dx[dir]
    ny = y + dy[dir]
    if apple[nx][ny] == 1:
        q.append([nx,ny])
        q.append([x,y])
    else :
        q.append([nx,ny])

    if 1 <= nx <= n and 1 <= ny <= n:
        break
    elif game[nx][ny] == 2:
        break

    sec += 1
    if sec == change[secCnt][0]:
        if change[secCnt][1] == 'D' :
            dir = (dir+1) % 4
        elif change[secCnt][1] =='L':
            if dir != 0 :
                dir -=1
            else :
                dir = 3

        secCnt += 1