


picks = [1,3,2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
n = len(minerals)
res = 0
tmp = [minerals[i:i+5] for i in range(0,len(minerals),5)]
if sum(picks) < len(tmp) :
    tmp = tmp[:sum(picks)]
# 광물이 더 많을 경우 => 뒤에는 못캐는데 정렬하면서 캐지게 되어버림
cnt = []
for t in tmp :
    cnt.append([t.count('diamond'),t.count('iron'),t.count('stone')])

cnt.sort(key=lambda x : (-x[0],-x[1],-x[2]))
#귀한 순서로 내림차순 정렬
idx = 0
flag = False
for i in range(3):
    for _ in range(picks[i]):
        if idx >= len(cnt) :
            flag = True
            break
        if i == 0 :
            res += sum(cnt[idx])
            idx += 1
        elif i == 1 :
            res += cnt[idx][0] * 5 + cnt[idx][1] + cnt[idx][2]
            idx += 1
        elif i == 2:
            res += cnt[idx][0] * 25 + cnt[idx][1] * 5 + cnt[idx][2]
            idx += 1
        
    if flag :
        break

print(res)




# from itertools import permutations

# picks = [1,3,2]
# minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# m_len = len(minerals)
# # 그리디 or 완전 탐색 => 완탐이 맞겠당
# picks = ['diamond'] * picks[0] +  ['iron'] * picks[1] + ["stone"] * picks[2]
# permutation = set(permutations(picks,len(picks)))
# res = 10 ** 9

# for p in permutation :
#     minerals_idx = 0
#     cnt = 0
#     for pick in p :

#         if minerals_idx >= m_len:
#             break

#         if pick == 'diamond' :
#             if minerals_idx + 5 < m_len:
#                 cnt += 5
#                 minerals_idx += 5
#                 continue
#             else :
#                 n = (m_len - minerals_idx +1)
#                 cnt += n
#                 minerals_idx += n
#                 continue

#         elif pick == 'iron' :
#             for i in range(5):
#                 if minerals_idx + i >= m_len :
#                     minerals_idx += i
#                     break
#                 else :
#                     if minerals[minerals_idx + i] == 'diamond' :
#                         cnt += 5
#                     else :
#                         cnt += 1
#             minerals_idx += 5

#         elif pick == 'stone' :
#             for i in range(5):
#                 if minerals_idx + i >= m_len :
#                     minerals_idx += i
#                     break
#                 else :
#                     if minerals[minerals_idx + i] == 'diamond' :
#                         cnt += 25
#                     elif minerals[minerals_idx + i] == 'iron' :
#                         cnt += 5
#                     else :
#                         cnt += 1
#             minerals_idx += 5
                    

#     res = min(res,cnt)

# print(res)



