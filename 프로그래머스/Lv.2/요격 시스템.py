


# max = len(targets), 나는 최소를 구해야한당
# targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	
# targets.sort(key = lambda x : (x[1] - x[0]))
# res = 0
# visited = [False] * (len(targets))

# for i in range(len(targets)) :
#     cnt = 0 
#     if not visited[i] :
#         visited[i] = True
#         cnt += 1
#         for j in range(i+1,len(targets)) :
#             tmp = [x for x in range(targets[j][0]+1,targets[j][1])]
#             #근데 아예 끝과 끝이 겹쳐있으면 안됨..
#             flag = False
#             for t in targets[i] :
#                 if t in tmp :
#                     flag  = True
#                 else : 
#                     continue
#             if not visited[j] and flag :
#                 visited[j] = True
#         res += cnt

# print(res)



targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	
targets.sort(key = lambda x : x[1])
print(targets)
res = 0
next = 0

for t in targets :
    if t[0] >= next :
        next = t[1]
        res += 1
print(res)