



n = int(input())
arr = list(map(int,input().split()))
dp = [a for a in arr]
# dp 는 증가 수열의 합 최대값을 저장해둘거! => ex. dp[3] = arr index=0~3 까지의 부분합을 써두는거

for i in range(1,n) :
    for j in range(i) :
        if arr[j] < arr[i] :
            dp[i] = max(dp[i],dp[j] + arr[i])


print(max(dp))