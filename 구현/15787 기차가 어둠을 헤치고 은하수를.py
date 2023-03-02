import sys
input = sys.stdin.readline

n,m = map(int,input().split())

train = [[0] * 21 for _ in range(n+1)]

for _ in range(m):
    cmd = list(map(int,input().split()))

    if cmd[0] == 1 :
        train[cmd[1]][cmd[2]] = 1
    elif cmd[0] == 2:
        train[cmd[1]][cmd[2]] = 0
    elif cmd[0] == 3:
        for i in range(20,0,-1) :
            train[cmd[1]][i] = train[cmd[1]][i-1]
    elif cmd[0] == 4:
        for i in range(1,20) :
            train[cmd[1]][i] = train[cmd[1]][i+1]
        train[cmd[1]][20] = 0

res = []

for i in range(1,n+1):
    if len(res) == 0 :
        res.append(train[i])
    else :
        # flag = False
        # for r in res :
        #     if r == train[i] :
        #         flag = True
        #     else :
        #         continue
        # if not flag :
        #     res.append(train[i])
        if train[i] not in res :
            res.append(train[i])

print(len(res))
