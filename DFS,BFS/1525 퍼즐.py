from collections import deque

puz = ''

for _ in range(3):
    puz += ''.join(list(input().split()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = {}

def bfs():
    q = deque([])
    visited[puz] = 0
    q.append(puz)

    while q :
        now = q.popleft()

        if now == '123456780':
            return visited[now]
        else :
            zero = now.index('0')
            #now.find() ??

            x = zero // 3
            y = zero % 3
            #문자열에서 2차원 리스트로 인덱스 뽑기

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<3 and 0<=ny<3 :
                    idx = nx *3 + ny
                    #0을 이동시킬 위치

                    tmp = list(now)
                    #문자열에서 리스트로 바꾼다음에 swap진행

                    tmp[zero],tmp[idx] = tmp[idx],tmp[zero]
                    new_puz = ''.join(tmp)
                    #1차원 리스트니까 걍 조인으로 다시 문자열로 만들어줌
                    
                    if not visited.get(new_puz):
                        #dict.get => key에 해당하는 값이 있으면 반환/ 없으면 none반환(오류x)
                        #이런식으로 방문 체크...
                        q.append(new_puz)
                        visited[new_puz] = visited[now] + 1

    return -1


print(bfs())

                        

