

n = 15
nums = [x for x in range(1,n+1)]
res = 0
sub_total = 0
end = 0




for start in range(len(nums)):
    while sub_total < n and end < len(nums) :
        sub_total += nums[end]
        end += 1
    if sub_total == n :
        res += 1 
    sub_total -= nums[start]


print(res)