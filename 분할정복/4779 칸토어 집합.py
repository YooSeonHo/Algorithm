import sys
sys.setrecursionlimit(10**6)

        

def kanto(n):
    if n == 0:
        return '-'
    line = kanto(n-1)
    lines = line+' '*len(line)+line

    return lines

while True:
    try:
        n = int(input())
        print(kanto(n))

    except EOFError:
        break

    