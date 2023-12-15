import sys
input = sys.stdin.readline
n = int(input())
init = [list(map(int,input().split())) for _ in range(n)]
stack = []
circle = []
for i in range(len(init)) :
    x,r = init[i]
    circle.append([x-r,i])
    circle.append([x+r,i])

circle.sort()

for i in range(len(circle)):
    if stack :
        if stack[-1][1] == circle[i][1] :
            stack.pop() 
            continue
    stack.append(circle[i])

if stack :
    print('NO')
else :
    print('YES')