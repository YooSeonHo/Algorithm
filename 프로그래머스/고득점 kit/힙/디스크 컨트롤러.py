from heapq import heapify, heappush, heappop

def solution(jobs):
    n = len(jobs)
    time = 0
    res = []
    
    heapify(jobs)
    
    while len(res) < n :
        tmp = []
        while jobs :
            start,how = heappop(jobs)
            if time < start :
                heappush(jobs,[start,how])
                break
            else :
                heappush(tmp,[how,start])
        
        if tmp :
            now = heappop(tmp)
            res.append(time - now[1] + now[0])
            time += now[0]
            while tmp :
                rejobs = heappop(tmp)
                heappush(jobs,[rejobs[1],rejobs[0]])
        else :
            time += 1
            
    return sum(res) // n