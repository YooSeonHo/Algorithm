import itertools
numbers = ['1','2','3','4','5','6','7','8','9']
res = list(itertools.permutations(numbers,3))

n = int(input())

for _ in range(n):
    num,s,b = input().split()
    s = int(s)
    b = int(b)
    
        
