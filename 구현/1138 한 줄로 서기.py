n = int(input())
arr = list(map(int,input().split()))
res = [0] * n


for i in range(n):
    jump = arr[i]
    #앞에 0을 jump개만큼 찾아야함
    cnt = 0
    #0찾을 때 마다 cnt++

    for j in range(len(res)):
        if res[j] == 0 :
            if jump == cnt :
                res[j] = i+1
                break
            else :
                cnt += 1

print(*res)
