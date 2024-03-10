from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    min_heap = []
    max_heap = []
    res = []
    visited = defaultdict(int)
    
    for o in operations :
        cmd = o.split()
        cmd[1] = int(cmd[1])
        
        if cmd[0] == 'I' :
            heappush(min_heap,cmd[1])
            heappush(max_heap,(-cmd[1],cmd[1]))
            visited[cmd[1]] += 1
            continue
            
        elif cmd[0] == 'D' and cmd[1] == 1 :
            #최대값 삭제
            while max_heap and not visited[max_heap[0][1]] :
                heappop(max_heap)
            if max_heap :
                visited[max_heap[0][1]] = 0
                heappop(max_heap)

        else :
            #최소값 삭제
            while min_heap and not visited[min_heap[0]] :
                heappop(min_heap)
            if min_heap :
                visited[min_heap[0]] = 0
                heappop(min_heap)     
                
    while max_heap :
        now = heappop(max_heap)[1]
        if visited[now] :
            res.append(now)
            break
    while min_heap :
        now = heappop(min_heap)
        if visited[now] :
            res.append(now)
            break
            
    if len(res) == 0 :
        return [0,0]
    elif len(res) == 1:
        return [res[0],res[0]]
    else :
        return res
