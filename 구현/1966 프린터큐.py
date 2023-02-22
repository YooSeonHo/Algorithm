from collections import deque
import copy
t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    im = list(map(int,input().split()))
    q = deque([])
    
    for i in range(n):
        q.append(i)
    res = 1
    tmp = copy.deepcopy(im)

    while q :
        v = q.popleft()
        
        if im[v] == max(tmp) :
            if v == m :
                print(res)
                break
            else :
                tmp.remove(im[v])
                res += 1
                continue
        else :
            q.append(v)

            