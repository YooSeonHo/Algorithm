

s = "(())()"
res = []
for i in range(len(s)):
    if s[i] == '(' :
        res.append(s[i])
    else :
        if len(res) == 0 :
            res.append(s[i])
            break
        else :
            if res[-1] == '(' :
                res.pop()
            else :
                res.append(s[i])

if len(res) == 0 :
    print(True)
else :
    print(False)