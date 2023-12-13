from itertools import combinations

exp = input().rstrip()
arr = []
idx = []
res = []

#괄호 인덱스 추출
for i in range(len(exp)) :
    if exp[i] == '(' :
        arr.append(i)
    elif exp[i] == ')' :
        index = arr.pop()
        idx.append([index,i])
    else :
        continue

for i in range(1,len(idx)+1) :
    com = list(combinations(idx,i))
    for c in com :
        tmp = exp
        p = []
        for e in c :
            a,b = e
            p.append(a)
            p.append(b)
        p.sort(reverse=True)
        for j in p :
            tmp = tmp[:j] + tmp[j+1:]
        res.append(tmp)

#중복 제거
res = sorted(list(set(res)))
print(*res,sep='\n')
