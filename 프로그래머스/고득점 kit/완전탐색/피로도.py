def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    res = []
            
    def backTracking(cnt,k) :
        
        for i in range(n) :
            if not visited[i] and k >= dungeons[i][0] :
                visited[i] = True
                k -= dungeons[i][1]
                cnt += 1
                backTracking(cnt,k)
                cnt -= 1
                visited[i] = False
                k += dungeons[i][1]
                
        res.append(cnt)
        return
                
    backTracking(0,k)
    return (max(res))