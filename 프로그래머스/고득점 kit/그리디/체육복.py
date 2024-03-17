def solution(n, lost, reserve):
    #중복 제거하고, 좌/우 확인
    
    lost.sort()
    reserve.sort()
    num = 0
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if lost[i] == reserve[j] :
                lost[i] = 0
                reserve[j] = 0
                num += 1
    res = n - len(lost) + num
    
    for i in range(len(lost)) :
        
        for j in range(len(reserve)) :
            if not lost[i] :
                break
            else :
                if lost[i]-1 and lost[i]-1 == reserve[j] :
                    res += 1
                    reserve[j] = 0
                    break
                elif lost[i]+1 and lost[i]+1 == reserve[j] :
                    res += 1
                    reserve[j] = 0
                    
    return (res)