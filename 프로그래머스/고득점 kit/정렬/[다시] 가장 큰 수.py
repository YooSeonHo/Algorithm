def solution(numbers):
    nums = list(map(str,numbers))
    nums.sort(key = lambda x : x*4,reverse = True)    
    res = "".join(nums)
    
    return res if int(res) else "0"