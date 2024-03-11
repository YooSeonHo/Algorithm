from itertools import permutations

def solution(numbers):
    n = 10000001
    res = 0
    
    primes = [True] * n
    visited = [False] * n
    primes[0] = False
    primes[1] = False
    # 1000만까지의 소수를 미리 결정 => 9가 7개 있는 경우까지 ㄱㄴ 9,999,999
    for i in range(2, int(n ** 0.5)+1) :
        if primes[i] :
            for j in range(2*i,n,i) :
                primes[j] = False
    
    for i in range(1,len(numbers)+1) :
        per = list(permutations(numbers,i))
        for p in per :
            check = int(''.join(p))
            if not visited[check] and primes[check] :
                res += 1
                visited[check] = True
    return (res)