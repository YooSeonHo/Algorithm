from collections import defaultdict
from itertools import combinations

def solution(clothes):
    arr = defaultdict(list)
    ans = 1
    
    for cloth,category in clothes :
        arr[category].append(cloth)
       
    for category in arr :
        ans *= (len(arr[category]) + 1)
    ans -= 1
    return ans
    
#     for i in range(len(arr),1,-1) :
#         com = list(combinations(arr,i))
#         for c in com :
#             tmp = 1
#             for cate in c :
#                 tmp *= len(arr[cate])
#             ans += tmp
#     return ans
            