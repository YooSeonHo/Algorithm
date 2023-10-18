



# # 원점에서부터 거리 (피타고라스로)가 큰 원의 반지름보다 작거나 같고,
# # 작은 원보다 크거나 같은지 체크, 이걸 4사분면중에 1사분면만 체크해서 *4 하면 된당 => 중복이 너무 많이 발생하는데;
# import math

# r1,r2 = 2,3
# res = 0

# for i in range(r2) :
#     if i == 0 :
#         res += (r2-r1+1) * 4
#         continue
#     for j in range(r2+1) :
#         if i == r1 and j == 0 :
#             continue
#         # 0,2 2,0이 중복되는데 체크되는중!!!!
#         #이렇게 하면 1,2 2,1 이 안세진당..........
#         di = []
#         di.append(math.sqrt(i ** 2 + j ** 2))
#         di.append(math.sqrt(((-i) ** 2) + j ** 2))
#         di.append(math.sqrt(i ** 2 + ((-j) ** 2)))
#         di.append(math.sqrt(((-i) ** 2) + ((-j) ** 2)))
#         for d in di :
#             if d <= r2 and d >= r1 :
#                 print(i,j)
#                 res +=1

# print(res)
