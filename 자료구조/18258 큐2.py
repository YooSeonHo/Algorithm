from collections import deque
import sys
input = sys.stdin.readline


q = deque([])

n = int(input())
for _ in range(n):
    cmd = list(input().split())

    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop' :
        if len(q) != 0 :
            popNum = q.popleft()
            print(popNum)
        else :
            print(-1)
    elif cmd[0] == 'size' :
        print(len(q))
    elif cmd[0] == 'empty' :
        print(1 if len(q) == 0 else 0)
    elif cmd[0] == 'front' :
        if len(q) != 0 :
            print(q[0])
        else :
            print(-1)
    elif cmd[0] == 'back' :
        if len(q) != 0 :
            print(q[-1])
        else :
            print(-1)
