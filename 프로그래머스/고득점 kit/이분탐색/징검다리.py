def solution(distance, rocks, n):
    start, end = 0, distance
    rocks.sort()
    rocks.append(distance)
    res = 0
    
    while start <= end :
        mid = (start+end)//2
        cnt = 0
        now = 0
        
        for r in rocks :
            if r - now < mid :
                cnt += 1
            else :
                now = r
            
            if cnt > n :
                break
        if cnt > n :
            end = mid - 1
        else :
            start = mid + 1
            res = mid
            
    return (res)
        