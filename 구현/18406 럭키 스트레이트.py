num = input()

cnt = len(num)
res1 = 0
res2 = 0

for i in range(0,cnt//2):
    res1 += int(num[i])
    res2 += int(num[i+(cnt//2)])

if res1 == res2 :
    print("LUCKY")
else : 
    print("READY")


# /2 => float, //2 => int