from collections import deque

def solution(priorities, location):
    proQ = deque([])
    idxQ = deque([])
    
    ans = 0
    for i in range(len(priorities)) :
        proQ.append(priorities[i])     
        idxQ.append(i)
        
    while proQ:
        ans += 1
        maxNum = max(proQ)
        
        while True :
            check = proQ.popleft()
            checkIdx = idxQ.popleft()
            if check == maxNum :
                if checkIdx == location :
                    return ans
                break
            proQ.append(check)
            idxQ.append(checkIdx)
            
        
        
