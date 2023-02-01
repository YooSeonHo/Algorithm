
s = input()
resToZ = 0
resToO = 0

cntToZ = 0
cntToO = 0

for i in s :
    if int(i) == 0 :
        if cntToZ > 0 :
            resToZ += 1
            cntToZ = 0
    else :
        cntToZ += 1

    if int(i) == 1 :
        if cntToO > 0 :
            resToO += 1
            cntToO = 0
    else :
        cntToO += 1

if cntToO > 0 :
    resToO += 1
if cntToZ > 0:
    resToZ += 1

print(min(resToZ,resToO))


#책 정답 -> 어렵당..
# data = input()
# cnt0 = 0
# cnt1 = 1

# if data[0] == '1' :
#     cnt0 += 1
# else :
#     cnt1 += 1


# for i in range(len(data)-1) :
#     if data[i] != data[i+1] :
#         if data[i+1] == '1' :
#             cnt0 += 1
#         else :
#             cnt1 += 1
# print(min(cnt0,cnt1))