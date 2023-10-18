

# plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
n = len(plans)
finish = []
for p in plans :
    hour = int(p[1].split(':')[0])
    minute = int(p[1].split(':')[1])
    p[1] = hour * 60 + minute
    p[2] = int(p[2])

plans.sort(key = lambda x : x[1])


for i in range(n) :
    delay = plans[i][1] + plans[i][2]
    for j in range(i+1,n) :
        if delay > plans[j][1] :
            delay += plans[j][2]
            continue
        else :
            break

    finish.append([i, plans[i][0], delay])

finish.sort(key = lambda x : [x[2],-x[0]])
res = [x[1] for x in finish]
print(res)