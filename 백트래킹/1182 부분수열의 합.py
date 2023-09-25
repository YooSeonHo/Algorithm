

n,s = list(map(int,input().split()))
nums = list(map(int,input().split()))
nums.sort()
cnt = 0

def backTracking(res,idx) :
    global cnt

    if res == s and idx >= 1 :
        cnt += 1

    if idx == n+1 :
        return
    else :
        for i in range(idx,n):
            res += nums[i]
            backTracking(res,i+1)
            res -= nums[i]

backTracking(0,0)
print(cnt)

