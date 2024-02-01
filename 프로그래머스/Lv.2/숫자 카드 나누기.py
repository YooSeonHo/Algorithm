from math import gcd
import copy

def solution(arrayA, arrayB):

    tmpA = copy.deepcopy(arrayA)
    tmpB = copy.deepcopy(arrayB)
    while len(arrayA) > 1 :
        arrayA.append(gcd(arrayA.pop(),arrayA.pop()))
    while len(arrayB) > 1 :
        arrayB.append(gcd(arrayB.pop(),arrayB.pop()))
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    res = []
    flag = False
    
    for a in tmpA :
        if a % gcdB == 0 :
            flag = True
            break
    if not flag :
        res.append(gcdB)
        
    flag = False
    
    for b in tmpB :
        if b % gcdA == 0 :
            flag = True
            break
    if not flag :
        res.append(gcdA)
        
    return (0 if not res else max(res))
        