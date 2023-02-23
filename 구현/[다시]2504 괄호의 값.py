s = input()

def check(st) :
    li = [] 
    for i in range(len(st)):
        if len(li) == 0 :
            li.append(st[i])
        else :
            a = li.pop()
            if a == '(' :
                if st[i] != ')':
                    li.append(a)
                    li.append(st[i])
            elif a == '[' :
                if st[i] != ']':
                    li.append(a)
                    li.append(st[i])
    if len(li) != 0 :
        return False
    else :
        return True

def cal(st) :
    li = []
    res = 0
    tmp = 1

    for i in range(len(st)):
        if s[i] == '(' :
            li.append(s[i])
            tmp *= 2
        elif s[i] == ')':
            if len(li) != 0 :
                a = li.pop()
                if a == '(':
                    if st[i-1] =='(':
                    # s[i-1] != '('면 이미 계산 된거!
                        res += tmp
                    tmp //= 2
        elif s[i] == '[':
            li.append(s[i])
            tmp *= 3
        elif s[i] == ']':
            if len(li) != 0 :
                a= li.pop()
                if a == '[':
                    if st[i-1] =='[':
                        res += tmp
                    tmp //= 3
    return res


#len이 0이 아닐때가 아니고 다른 방법이 필요함!!!!!!!!!!!!!!!

if not check(s) :
    print(0)
else :
    print(cal(s))
    
                