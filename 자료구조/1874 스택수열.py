import sys
input = sys.stdin.readline

n = int(input())
res = []
idx = 1
flag = False

nums = [int(input()) for _ in range(n)]
stack = []

for i in range(n):
    num = nums[i]
    while idx <= num :
        res.append('+')
        stack.append(idx)
        idx += 1

    if stack[-1] > num :
        flag = True
        break
    
    while True :
        n = stack.pop()
        res.append('-')
        if n == num :
            break

if flag :
    print('NO')
else :
    print(*res,sep='\n')

        

