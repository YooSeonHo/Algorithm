# n = int(input())
# arr = list(map(int,input().split()))
# inDp = [1]*n
# deDp = [1]*n
# hap = list()

# for i in range(1,n):
#     for j in range(i):
#         if arr[j]<arr[i]:
#             inDp[i] = max(inDp[i],inDp[j]+1)

# for i in range(n-1,-1,-1):            
#     for j in range(n-1,i,-1):
#         if arr[j]<arr[i]:
#             deDp[i] = max(deDp[i],deDp[j]+1)

    
# for i in range(n):
#     hap.append(inDp[i]+deDp[i]-1)

# print(max(hap))
        
