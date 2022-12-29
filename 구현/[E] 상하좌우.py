dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
arr = list(input().split())

""" now = [1,1]

for i in range(len(arr)):
    if arr[i] == 'R':
        if now[1] == n :
            continue
        else :
            now[1] +=1
            continue
    elif arr[i] == 'L':
        if now[1] == 1:
            continue
        else :
            now[1] -=1
            continue
    elif arr[i] == 'U' : 
        if now[0] == 1:
            continue
        else :
            now[0] -=1
            continue
    else :
        if now[0] == n:
            continue
        else:
            now[0] +=1
            continue

print(now[0],now[1])

# ㅋㅋ 장난? 이딴식으로 짜지 마세요. 네. """

move = ['R','L','D','U']
x,y = 1,1

for i in arr :
    for j in range(len(move)):
        if i == move[j] :
            nx = x + dx[j]
            ny = y + dy[j]
    if nx<1 or ny <1 or nx >n or ny>n:
        continue
    x = nx
    y = ny

print(y,x)