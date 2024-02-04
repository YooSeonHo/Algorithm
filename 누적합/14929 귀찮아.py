n = int(input())
arr = list(map(int,input().split()))

ans = 0
# for i in range(len(arr)):
#     ans += arr[i] * sum(arr[i+1:])
# print(ans)
# 시간 초과

hap = [arr[0]]
for i in range(1,n) :
    hap.append(hap[-1] + arr[i])

for i in range(n) :
    ans += arr[i] * (hap[i]-arr[i])
print(ans)