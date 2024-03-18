def solution(number, k):
    n = len(number)
    cnt = 0
    number = list(map(int,number))
    stack = []
    flag = False
    
    for i in range(n) :
        if not stack :
            stack.append(number[i])
            continue
        while stack and stack[-1] < number[i] :
            cnt += 1
            stack.pop()
            
            if cnt == k :
                flag = i
                break
                
        stack.append(number[i])
        if flag :
            break
            
    if not flag :
        while cnt < k :
            number.pop()
            cnt += 1
        return ''.join(map(str,number))
            
    return (''.join(map(str,stack + number[i+1:])))
