k = int(input())
res = []

for _ in range(k):
    s = int(input())
    if len(res) >= 1 and s == 0 :
        res.pop()
    else :
        res.append(s)

print(sum(res))