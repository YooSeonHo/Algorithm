def solution(storey):
    res = 0
    storey = list(map(int,str(storey)))
    n = len(storey)
    
#DP로 풀면 풀릴 거 같은데 => 근데 10억갠데 메모리 터질듯..
    
# 단순 구현
    for i in range(n-1,-1,-1) :
        print(res,storey[i])
        if i == 0 :
            #마지막에서도, 무조건 다 빼버리는게 아니라 마지막 자릿수 까지 체크를 해야함
            if storey[0] > 5 :
                res += (10 - storey[0]) + 1
            else :
                res += storey[0]
            break
        
        #더하는 경우 
        if storey[i] > 5 or (storey[i] == 5 and storey[i-1] >= 5 ):
            res += (10 - storey[i])
            storey[i-1] += 1
            
        #빼는 경우
        else :
            res += storey[i]
            
    return (res)

print(solution(945))