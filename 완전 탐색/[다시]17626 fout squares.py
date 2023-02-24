from itertools import combinations_with_replacement
from math import sqrt
n = int(input())
sq1 = [i*i for i in range(1,int(sqrt(n))+1)]
sq2 = [sum(n) for n in combinations_with_replacement(sq1,2)]

def four(n) : 
    if n in sq1 :
        print(1)
        return
    elif n in sq2 :
        print(2)
        return 
    else :
        for sq in sq1 :
            if (n-sq) in sq2 :
                print(3)
                return
    print(4)

four(n)