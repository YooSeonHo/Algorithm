import sys
from collections import deque
imput = sys.stdin.readline

def DSLR(A,B):
    res = []
    q = deque([])
    q.append(A)

    while q:
        x = q.popleft()
        if x == B:
            print(''.join(res))
            return
        else:
            


T = int(imput())

for i in range(T):
    A,B = map(int,imput().split())

        