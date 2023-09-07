from collections import deque

n = int(input())
ballons = list(map(int,input().split()))
q = deque()

for i in range(len(ballons)) :
    q.append((i+1,ballons[i]))

res = []

while len(q) > 0 :
    num,cnt = q.popleft()
    res.append(num)
    if len(q) == 0 : 
        break
    if cnt > 0 :
        for i in range(1,cnt):
            q.append(q.popleft())
    else :
        for i in range(0,cnt,-1):
            q.appendleft(q.pop())


print(*res)

