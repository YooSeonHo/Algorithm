def solution(brown, yellow):
    
    # i = 세로, b = 가로
    for i in range(1, yellow+1) :
        if yellow % i != 0 : 
            continue
        b = yellow // i
        if (b + 2) * 2 + i * 2 == brown :
            return [b+2,i+2]
        
        