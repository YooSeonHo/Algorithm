import math

def solution(n, words):
    
    flag = False
    stack = []
    
    for w in words :
        if not stack :
            stack.append(w)
            continue
        
        if w in stack :
            flag = True
            # 차라리 여기서 append 하지 말고, a 계산할 때 len(stack) // n + 1 로 하는 게 더 좋았을 듯
            stack.append(w)
            break
        
        if stack[-1][-1] != w[0] :
            flag = True
            # 차라리 여기서 append 하지 말고, a 계산할 때 len(stack) // n + 1 로 하는 게 더 좋았을 듯
            stack.append(w)
            break
        stack.append(w)
        
    if not flag :
        return ([0,0])
    else :
        a = math.ceil(len(stack) / n)
        b = len(stack) % n
        if b == 0 :
            b = n
            
        return [b,a]
        
            