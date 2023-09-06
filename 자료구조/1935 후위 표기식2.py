from collections import deque

n = int(input())
s = list(input().rstrip())
nums = [int(input()) for _ in range(n)]
q = deque([])

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z' :
        s[i] = nums[ord(s[i])-65]

for i in range(len(s)):
    if isinstance(s[i],(int,float)) :
        q.append(s[i])
    else :
        b,a = q.pop(), q.pop()
        
        tmp = 0
        if s[i] == '*' :
            tmp = a * b
        elif s[i] == '+' :
            tmp = a+b
        elif s[i] == '/' :
            tmp = a/b
        elif s[i] == '-':
            tmp = a-b
        q.append(tmp)

print(format(q[0],".2f"))
        