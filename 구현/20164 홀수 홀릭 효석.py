

num = int(input())
ans = []
def count_odd(num) :
    cnt = 0
    odds = ['1','3','5','7','9']
    num = str(num) 
    for n in num :
        if n in odds :
            cnt += 1
        else :
            continue

    return cnt

def sol(num,cnt) :
    cnt += count_odd(num)

    if num < 10 :
        ans.append(cnt)
        return cnt
    elif 10<= num < 100 :
        tmp = str(num)
        num = int(tmp[0]) + int(tmp[1])
        sol(num,cnt)
    else :
        num = str(num)
        for i in range(1,len(num)) :
            for j in range(i+1,len(num)):
                tmp = int(num[:i]) + int(num[i:j]) + int(num[j:])
                sol(tmp,cnt)


sol(num,0)
print(min(ans), max(ans))
