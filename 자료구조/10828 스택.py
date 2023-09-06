import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    cmd = list(input().split())

    if cmd[0] == 'push' : 
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop' :
        if (stack) :
            popNum = stack.pop()
            print(popNum)
    
        else :
            print(-1)
        
    elif cmd[0] == 'size' : 
        print(len(stack))
    elif cmd[0] == 'empty' :
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == 'top' :
        print(-1 if len(stack)== 0 else stack[len(stack)-1])
