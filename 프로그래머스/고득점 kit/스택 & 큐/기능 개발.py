from collections import deque

def solution(progresses, speeds):
    proQ = deque(progresses)
    speedQ = deque(speeds)
    res = []
    
    while proQ :
        n = 100 - proQ[0]
        mod = 0
        if n % speedQ[0] :
            mod += 1
        
        n = n // speedQ[0]
        n += mod
        # n일 후 배포
        
        for i in range(len(proQ)) :
            proQ[i] += speedQ[i] * n
        
        cnt = 0
        for i in range(len(proQ)) :
            if proQ[i] >= 100 :
                cnt += 1
            else : break
        for i in range(cnt):
            proQ.popleft()
            speedQ.popleft()
        res.append(cnt)
        
    return (res)