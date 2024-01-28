from collections import defaultdict
def solution(weights):
    n = len(weights)
    dic = defaultdict(int)
    res = 0
    
    for w in weights :
        dic[w] += 1
        
    for d in list(dic) : 
        print(d, dic[d])
        if dic[d] > 1 :
            res += (dic[d] * (dic[d]-1)) // 2
            
        res += ( dic[d * 4/ 3 ] * dic[d])
        res += (dic[d * 2] * dic[d])
        res += ( dic[d * 3 / 2 ] * dic[d])
        
    return (res)