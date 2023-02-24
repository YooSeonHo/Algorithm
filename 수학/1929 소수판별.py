import sys

def is_prime(a,b):
    p = [True] * (b+1)
    p[0] = False
    p[1] = False
    
    for i in range(2,int(b**0.5)+1):
        if p[i] == True :
            for j in range(2*i,b+1,i):
                #i가 소수라면(True) b전까지 i배수 애들을 False로
                p[j] = False

    return [i for i in range(a,b+1) if p[i]]            
                
        
a,b = map(int,sys.stdin.readline().split())

ans = is_prime(a,b)
for i in ans:
    print(i)
