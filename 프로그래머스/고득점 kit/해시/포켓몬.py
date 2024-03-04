
def solution(nums):
    n = len(nums)//2
    ans = 0
    nums = set(nums)
    
    if len(nums) >= n :
        ans = n
    else :
        ans = len(nums)
        
    return ans