import sys
input = sys.stdin.readline
n=int(input())

for _ in range(n):
    pt = list(input().rstrip())
    stack = []

    for i in range(len(pt)):
        if pt[i] == '(' :
            stack.append(pt[i])
        else :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(pt[i])

    print('YES' if len(stack) == 0 else 'NO')