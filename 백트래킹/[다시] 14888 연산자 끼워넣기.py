from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))
ops = list(map(int,input().split()))
op = '+' * ops[0] + '-' * ops[1] + '*' * ops[2] + '/' * ops[3]
per = permutations(op,n-1)
ans = []

for p in per :
    res = nums[0]

    for i in range(1,n) :
        if p[i-1] == '+' :
            res += nums[i]
        if p[i-1] == '-' :
            res -= nums[i]
        if p[i-1] == '*' :
            res *= nums[i]
        if p[i-1] == '/' :
            if res < 0 :
                res = abs(res) // nums[i] 
                res = -res
            else :
                res //= nums[i]

    ans.append(res)


print(max(ans),min(ans))
    
###############################################################
# pypy3 로 제출해야 시간 초과 안남......... 백 트래킹으로 풀어보자 ########
###############################################################


import sys
sys.setrecursionlimit(10**6)
n = int(input())
nums = list(map(int,input().split()))
add,sub,mul,div = list(map(int,input().split()))
ans = []

def backTracking(add,sub,mul,div,res,idx) :
    if idx == n :
        ans.append(res)
        return

    else :
        if add :
            backTracking(add-1,sub,mul,div,res+nums[idx],idx+1)
        if sub :
            backTracking(add,sub-1,mul,div,res-nums[idx],idx+1)
        if mul :
            backTracking(add,sub,mul-1,div,res*nums[idx],idx+1)
        if div :
            if res < 0 :
                res = abs(res) // nums[idx]
                res = -res
            else :
                res //= nums[idx]
            backTracking(add,sub,mul,div-1,res,idx+1)

backTracking(add,sub,mul,div,nums[0],1)
print(max(ans),min(ans))