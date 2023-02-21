n = int(input())

for _ in range(n):
    s = input()
    res = 0
    sub = 0
    for i in range(len(s)):
        if s[i] == 'O':
            sub += 1
            res += sub
        else :
            sub = 0
    print(res)
    
    