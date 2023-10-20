
from collections import defaultdict


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
book_time.sort(key = lambda x : (x[0],x[1]))
for b in book_time :
    hour = int(b[0].split(':')[0]) * 60
    time = hour + int(b[0].split(':')[1])
    b[0] = time
    hour = int(b[1].split(':')[0]) * 60
    time = hour + int(b[1].split(':')[1])
    b[1] = time

res = defaultdict(str)
idx = 1

for b in book_time :
    if len(res) == 0:
        res[idx] = b[1]
        idx += 1
    else :
        flag = False
        for i in range(1,len(res)+1) :
            if res[i] + 10 <= b[0] :
                res[i] = b[1]
                flag = True
                break
        if not flag :
            res[idx] = b[1]
            idx += 1

print(len(res))
            