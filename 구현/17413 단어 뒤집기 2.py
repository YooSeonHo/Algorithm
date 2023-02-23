s = input()
flag = False
li = []

for i in range(len(s)):

    if not flag and s[i] == ' ' :
        for _ in range(len(li)) :
            print(li.pop(),end='')
        print(' ',end='')
        continue

    if s[i] == '<':
        if len(li) != 0 :
            for _ in range(len(li)) :
                print(li.pop(),end='')

        flag = True
        print('<',end='')
        continue
    elif s[i] == '>':
        flag = False
        print('>',end='')
        continue
    else :
        if flag :
            print(s[i],end='')
            continue
        else :
            li.append(s[i])

if len(li) != 0 :
    for _ in range(len(li)) :
        print(li.pop(),end='')