import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [0] + list(map(int,input().split()))
dp = [[0] * (k+1) for _ in range(n+1)] #[1~N][삭제 횟수]

for i in range(1,n+1) :
    for j in range(k+1) :
        if arr[i] % 2 == 0 :
            dp[i][j] = dp[i-1][j] + 1
        
        else :
            if j != 0 :
                dp[i][j] = dp[i-1][j-1] 
print(dp)