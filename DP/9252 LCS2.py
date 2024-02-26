import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
n,m = len(a),len(b)

dp = [[""] * (m+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,m+1) :
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else :
            if len(dp[i-1][j]) > len(dp[i][j-1]) :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]
                
cnt = len(dp[-1][-1])
print(cnt)
if cnt > 0 :
    print(dp[-1][-1])