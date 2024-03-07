
def solution(prices):
    res = []
    n = len(prices)
    
    # 완전 탐색
    for i in range(n-1) :
        cnt = 0
        now = prices[i]
        for j in range(i+1,n) :
            if now > prices[j] :
                cnt += 1
                break
            cnt += 1
        res.append(cnt)
    res.append(0)    
    return (res)
    
    #stack 사용 
    ans = [0] * n
    stack = []

    for i in range(n-1) :
        now = prices[i]
        while stack and prices[stack[-1]] > now :
            m = stack.pop() 
            ans[m] = i - m
        stack.append(i)
        
    #남아 있는 stack 처리
    while stack :
        m = stack.pop()
        ans[m] = n - 1 - m
    return (ans)