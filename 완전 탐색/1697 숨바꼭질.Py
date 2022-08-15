import sys
from collections import deque
imput = sys.stdin.readline

n,k = list(map(int,imput().split()))
MAX = 100000
time = [0] * (MAX+1)

def bfs():
    q = deque([])
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(time[x])
            break
        else:
            for i in (x-1,x+1,x*2):
                #와 신기한 for문
                if 0<=i<=MAX and not time[i]:
                    #bfs, tree 이런건 최대한 지우고 조건을 잘 생각해야 하는듯,..
                    time[i] = time[x]+1
                    q.append(i)


bfs()