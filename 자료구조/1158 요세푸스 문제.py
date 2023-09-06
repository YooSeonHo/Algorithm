from collections import deque

n,k = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])
res = []


while len(q) > 0 :
    for i in range(1,k+1) :
        if i == k :
            res.append(q.popleft())
        else :
            q.append(q.popleft())

print('<',end='')
print(*res, sep=', ',end='')
# 이렇게 하면 사이에만 ,가 붙고 맨 끝에는 안붙네 개신기
print('>')
