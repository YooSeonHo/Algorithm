from collections import deque
a,b = map(int,input().split())

# 2를 곱하거나 1을 더하거나 => 걍 bfs로 다 queue에 넣고 !
# 어떤 상태에 도달하기 -> bfs 생각해보기 (그래프탐색)
# visited = [False] * (b+1)

def bfs():
    q = deque([])
    q.append((a,1))
    # visited[a] = True
    
    while q:
        now,cnt = q.popleft()
        if now == b :
            return cnt
        else :
            if now*2 <= b:
            # if now*2 <= b and not visited[now*2] :
                q.append((now*2,cnt+1))
                # visited[now*2] = True
            if (now*10+1) <= b :
            # if (now*10+1) <= b and not visited[now*10+1] :
                q.append((now*10+1,cnt+1))
                # visited[now*10+1] = True

    return -1

print(bfs())