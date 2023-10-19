



s = "110010101001"
cnt = 0
zero = 0
nums = list(map(int,s))

while len(nums) > 1 :
    tmp = len(nums) - sum(nums)
    zero += tmp
    nums = '1' * (len(nums)-tmp)
    nums = bin(len(nums))[2:]
    nums = list(map(int,nums))
    print(nums)
    cnt += 1

print([cnt,zero])

    