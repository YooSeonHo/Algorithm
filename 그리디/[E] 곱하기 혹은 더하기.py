s = input()
res = int(s[0])

for i in range(1,len(s)) :
    num = int(s[i])
    if res <= 1 or num <=1 :
        res += num
    else :
        res *= num

print(res)