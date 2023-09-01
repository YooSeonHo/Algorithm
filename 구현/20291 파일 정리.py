from collections import Counter

n = int(input())

files = [input() for _ in range(n)]
ex = []
for i in range(len(files)) :
    ex.append(files[i].split('.')[1])

cnt = list(Counter(ex).items())
#Counter 객체를 리스트화

cnt.sort(key = lambda x : x[0])

for i in cnt :
    print(i[0], i[1])