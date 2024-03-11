def solution(sizes):
    n = len(sizes)
    
    max_w = 0
    max_h = 0
    
    
    
    for i in range(n) :
        sizes[i].sort()
        if max_w < sizes[i][0] :
            max_w = sizes[i][0]
        if max_h < sizes[i][1] :
            max_h = sizes[i][1]
            
    return max_w * max_h