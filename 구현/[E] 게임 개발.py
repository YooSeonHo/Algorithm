import sys
imput = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int,imput().split())
row,col,dir = map(int,imput().split())
arr = [list(map(int,imput().split())) for _ in range(n)]
# 2차원 배열 입력받기

"""
cnt = 1
arr[row][col] = 1

 while True :
    for i in range(4):
        nx = row + dx[dir % 4]
        ny = col + dy[dir % 4]

        if arr[nx][ny] == 1 or nx < 0 or ny < 0 or nx > m or ny > n :
            dir += 1
            continue
        else :
            cnt += 1
            arr[nx][ny] = 1
            dir = dir%4
            row = nx
            col = ny
            break

        #이런 식으로 짜면 다시 돌아가지 못함 다시!
    if dir >= 4:
        break
print(cnt)
 """
        
#왜 두개의 배열이 필요한가? => 이미 방문했다면 1로 표시해야함 -> 근데 뒤가 바다일 땐 게임을 종료 -> 만약 배열이 하나라면 바다여서 1인건지 방문해서 1인건지 알 수 x -> 그래서 visited배열을 만드는거

visited = [[0] * m for _ in range(n)]
visited[row][col] = 1
res = 1
cnt = 0

while True:
    dir -=1
    if dir == -1 :
        dir = 3

    nx  = row + dx[dir]
    ny  = col + dy[dir]

    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        res +=1
        visited[nx][ny] = 1
        row = nx
        col = ny
        cnt = 0
        continue
    else :
        cnt +=1

    if cnt == 4:
        #"방향을 유지하고 뒤로 간다"인데 대체 왜 빼지? ㅋㅋ => 내가 갈 방향을 빼면 뒤로 가는거니까!! 말로 설명하기 조금 어렵덩
        row -= dx[dir]
        col -= dy[dir]

        if arr[row][col] == 1:
            break
        else:
            cnt = 0
print(res)