# import sys
# from collections import deque, Counter
# input = sys.stdin.readline

# n,k = map(int,input().split())
# arr = list(map(int,input().split()))
# ans = deque([])
# length = 0
# s,e = 0, 0

# def check(num) :
#     global k, ans
#     counter = Counter(ans)[num]
#     if counter >= k :
#         #k개가 이미 포함되어 있으면 더이상 포함 시키면 안됨 => True 반환 => s를 이동 시켜야함
#         return True
#     else :
#         return False


# while e < n :

#     if not check(arr[e]) :
#         ans.append(arr[e])
#         e += 1
#     else :
#         ans.popleft()
#         s += 1
    
#     length = max(length,len(ans))

# print(length)



import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = defaultdict(int)
length = 0
s,e = 0, 0


while e < n :
    if ans[arr[e]] >= k :
        ans[arr[s]] -= 1
        s += 1

    else :
        ans[arr[e]] += 1
        e += 1
    length = max(length,e-s)

print(length)