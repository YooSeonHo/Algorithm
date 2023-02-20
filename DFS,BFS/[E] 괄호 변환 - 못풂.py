from collections import deque
def absol(s):
    if len(s) == 0 :
        return True
    else :
        tmp = []
        tmp.append(s[0])
        for i in range(1,len(s)):
            if s[len(tmp)-1] == '(' and s[i] == ')':
                tmp.pop()
            else :
                tmp.append(s[i])
    if len(tmp) == 0 :
        return True
    else :
        return False
    
def bal(s):
    left = 0
    right = 0
    for i in s:
        if i == '(' :
            left += 1
        else :
            right += 1
        if left == right :
            return left+right
        
def solution(p):
    
    if len(p) == 0 :
        return
    else :
        div = bal(p)
        u = p[:div]
        v = p[div:]
        
        solution(u)



        
#https://school.programmers.co.kr/learn/courses/30/lessons/60058