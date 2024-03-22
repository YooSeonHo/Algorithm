def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,n) :
        for j in range(i+1) :
            if j == 0 :
                dp[i][j] = dp[i-1][j] + triangle[i][0]
                continue
            if j == i :
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                continue
                
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
            
    return (max(dp[-1]))