def solution(answers):
    n = len(answers)
    one = [1,2,3,4,5] * n
    two = [2,1,2,3,2,4,2,5] * n
    three = [3,3,1,1,2,2,4,4,5,5] * n
    ans_one = [0] * n
    ans_two = [0] * n
    ans_three = [0] * n
    
    for i,a in enumerate(answers) :
        if a == one[i] :
            ans_one[i] = 1
        if a == two[i] :
            ans_two[i] = 1
        if a == three[i] :
            ans_three[i] = 1
    a = sum(ans_one)
    b = sum(ans_two)
    c = sum(ans_three)
    candidate = max(a,b,c)
    res = []
    
    if candidate == a :
        res.append(1)
    if candidate == b :
        res.append(2)
    if candidate == c :
        res.append(3)
        
    return res
            