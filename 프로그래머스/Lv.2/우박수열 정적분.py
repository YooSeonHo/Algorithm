def solution(k, ranges):
    idx = 0
    g = []
    while k != 1 :  
        g.append([idx,k])
        if k % 2 == 0:
            k //= 2
        else :
            k = 3 * k + 1
        idx += 1
    g.append([idx,1])
    
    block = []
    for i in range(len(g)-1) :
        block.append((g[i][1] + g[i+1][1])/2)
        
    n = len(block)
    res = []
    for r in ranges :
        a = r[0]
        b = n + r[1]
        if a > b:
            res.append(-1.0)
        else : 
            res.append(sum(block[a:b]) if sum(block[a:b]) else 0.0)
        
    return (res)