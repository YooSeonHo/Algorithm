import copy
from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
res = 0
visited = [[False] * m for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
max_value = max(map(max,arr))

def dfs(y,x,ans,cnt):
    global res
    #만약 남은 블록을 다 최대값으로 더해도 현재 최대값보다 작으면 걍 조기 종료
    #이런 조기 종료 규칙이 진심 시간 복잡도 확 줄여줌..
    if res >= ans + max_value * (4-cnt) : 
        return
    if cnt == 4 :
        res = max(res,ans)
        return

    else :
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not visited[ny][nx] :

                if cnt == 2 :
                    # ㅗ 모양 체크
                    visited[ny][nx] = True
                    dfs(y,x,ans+arr[ny][nx],cnt+1)
                    visited[ny][nx] = False
                #나머지 모든 모양 체크
                visited[ny][nx] = True
                dfs(ny,nx,ans+arr[ny][nx],cnt+1)
                visited[ny][nx] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,arr[i][j],1)
        visited[i][j] = False

print(res)



# long_dy = [3,0]
# long_dx = [0,3]
# visited = [[False] * m for _ in range(n)]
# res = 0

# def long_check(visited_original):
#     global res
#     visited = copy.deepcopy(visited_original)
#     q = deque([])
#     q.append([0,0])

#     while q :
#         y,x = q.popleft()
#         visited[y][x] = True 

#         for i in range(2):
#             ny = y + long_dy[i]
#             nx = x + long_dx[i]

#             if 0<=ny<n and 0<=nx<m :
#                 tmp = 0
#                 if i == 0 :
#                     tmp += arr[y][nx]
#                     tmp += arr[y+1][nx]
#                     tmp += arr[y+2][nx]
#                     tmp += arr[y+3][nx]
#                 else :
#                     tmp += arr[ny][x]
#                     tmp += arr[ny][x+1]
#                     tmp += arr[ny][x+2]
#                     tmp += arr[ny][x+3]
#                 res = max(res,tmp)

#                 if x == m-1 :
#                     q.append([y+1,0])
#                 else :
#                     q.append([y,x+1])

# long_check(visited)
# print(res)


