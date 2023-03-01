s = input()
res = 0

tmp = ''
flag = False
for i in range(len(s)):
    if '0'<=s[i]<='9':
        tmp += s[i]
    elif s[i] == '+':
        if flag :
            res -= int(tmp)
            tmp = ''
        else :
            res += int(tmp)
            tmp = ''
    else :
        if flag : 
            res -= int(tmp)
            tmp = ''
        else :
            flag = True
            res += int(tmp)
            tmp = ''
if flag :
    res -= int(tmp)
else :
    res += int(tmp)

print(res)
