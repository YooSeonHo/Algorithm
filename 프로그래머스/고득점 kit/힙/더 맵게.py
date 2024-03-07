from heapq import heappush, heappop, heapify

def solution(scoville, K):
    cnt = 0
    heapify(scoville)
    
    while len(scoville) >= 2 :
        n = heappop(scoville)
        m = heappop(scoville)
        
        if n >= K :
            return cnt
        
        new = n + m * 2
        cnt += 1
        heappush(scoville,new)
    
    if scoville and scoville[-1] >= K :
        return cnt
        
    return -1