def solution(n, times):
    start,end = 1 , max(times) * n
    res = 0
    
    while start <= end :
        mid = (start+end) // 2 
        
        check = 0
        for t in times :
            check += mid // t
            
            if check >= n :
                break
        
        if check >= n :
            end = mid - 1
            res = mid
        else :
            start = mid + 1
    
    return (res)
