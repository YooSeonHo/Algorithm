from collections import defaultdict

def solution(k, tangerine):
    dic = defaultdict(int)
    for t in tangerine :
        dic[t] += 1
        
    dic = sorted(dic.items(), key = lambda x : x[1], reverse=True)
    
    now = 0
    res = 0
    for d in dic :
        if now >= k :
            break
        now += d[1]
        res += 1
        
    return (res)