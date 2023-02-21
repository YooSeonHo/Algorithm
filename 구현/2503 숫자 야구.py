import itertools
numbers = ['1','2','3','4','5','6','7','8','9']
res = list(itertools.permutations(numbers,3))

n = int(input())

for _ in range(n):
    num,s,b = input().split()
    s = int(s)
    b = int(b)
    idx = 0
    
    for r in range(len(res)) :
        strake = 0
        ball = 0
        r -= idx
        for i in range(3):
            if res[r][i] == num[i] :
                strake += 1
            elif num[i] in res[r] :
                ball += 1

        if strake != s or ball != b :
            res.remove(res[r])
            idx += 1

print(len(res))
