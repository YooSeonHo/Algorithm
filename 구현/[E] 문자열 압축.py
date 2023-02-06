def solution(s):
    
    if (len(s) == 1) :
        return 1
    min = 1001
    for i in range(1,len(s)//2+1):
        cnt = 1
        res = ''
        #i개 단위로 자르는거
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+(2*i)] :
                cnt +=1
            else :
                if cnt == 1 :
                    res += s[j:j+i]
                else :
                    res += str(cnt) + s[j:j+i]
                    cnt = 1

        if len(res) < min :
            min = len(res)
    return min