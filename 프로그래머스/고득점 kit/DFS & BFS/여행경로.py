from collections import defaultdict,deque

def solution(tickets):
    
    tics = defaultdict(list)
    visited = defaultdict(int)
    
    for t in tickets :
        visited[t[0]+t[1]] += 1
    
    res = []
    n = len(tickets) + 1
    
    for t in tickets :
        a,b = t
        tics[a].append(b)
         
    def back_tracking(where) :
        res.append(where)
        if len(res) == n :
            return res
        
        tics[where].sort()
        for go in tics[where] :
            if visited[where+go] > 0 :
                visited[where+go] -= 1
                back_tracking(go)
                if len(res) == n :
                    return res
                visited[where+go] += 1
                res.pop()

    res = back_tracking('ICN')
    return res