

n,m = list(map(int,input().split()))
#nCm을 출력 => n! / (n-m)! * m!

square = [0] * 101
square[1] = 1

for i in range(2,n+1) :
    square[i] = square[i-1] * i


print(square[n]//(square[n-m] * square[m]))