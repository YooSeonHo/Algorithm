n = int(input())

tip = []
for _ in range(n):
    tip.append(int(input()))

res = 0
tip.sort(reverse=True)

for i in range(n):
    t = tip[i] - i
    if t > 0 :
        res += t
    else : 
        break

print(res)