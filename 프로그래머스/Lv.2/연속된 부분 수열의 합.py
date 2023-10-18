


sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
res = []
n = len(sequence)

# 이중 포문을 쓰면 안된당
s,e = 0,0
sub_total = 0

for s in range(n) :
    while sub_total < k and e < n :
        sub_total += sequence[e]
        e += 1
    if sub_total == k :
        res.append([s,e-1])
    sub_total -= sequence[s]



res.sort(key = lambda x : (x[1]-x[0],x[0]))
print(res[0])

