def solution(s):
    stack = []
    
    for st in s :
        if not stack :
            stack.append(st)
            continue
        
        if stack[-1] == st :
            stack.pop()
        else :
            stack.append(st)
            
    return (1 if not stack else 0)
        