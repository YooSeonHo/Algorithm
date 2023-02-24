# from itertools import combinations
t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    # arr = [i for i in range(m)]
    # num = list(combinations(arr,n))
    # print(len(num))
    if n == m :
        print(1)
        continue
    tmp = min(n,m-n)

    up = 1
    down = 1
    for i,j in zip(range(m,tmp,-1),range(tmp,0,-1)):
        up *= i
        down *= j
    print(int(up/down))
    
