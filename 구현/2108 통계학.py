from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

print(round(sum(arr)/len(arr)))
#1

arr.sort()
print(arr[len(arr)//2])
#2

if len(arr) == 1 :
    print(arr[0])
else :
    cnt = Counter(arr).most_common(2)
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
        #arr => 이미 정렬되어있음 ㅋ
    else :
        print(cnt[0][0])

# else :
    # res = [(arr[0],1)]
    # for i in range(1,len(arr)):
    #     if arr[i-1] == arr[i]:
    #         res.append((arr[i],res[i-1][1]+1))
    #     else :
    #         res.append((arr[i],1))
    # res.sort(key= lambda x : x[1], reverse=True)
    # for i in range(1,len(res)):
    #     if res[i-1][1] == res[i][1] :
    #         continue
    #     else :
    #         print(res[i-1][0])
    #         break
# else :
#     res = []
#     for i in range(len(arr)):
#         cnt = 0
#         for j in range(len(arr)):
#             if arr[i] == arr[j] :
#                 cnt +=1
#         res.append(cnt)
#     index = []
#     for i in range(len(res)):
#         if res[i] == max(res):
#             index.append(i)
    
#     if len(index) == 1:
#         print(index[0])
#     else :
#         tmp = []
#         for i in range(len(index)):
#             if arr[index[i]] not in tmp:
#                 tmp.append(arr[index[i]])
#         if len(tmp) == 1 :
#             print(tmp[0])
#         else:
#             tmp.sort()
#             print(tmp[1])

#3
print(max(arr)-min(arr))
#4
