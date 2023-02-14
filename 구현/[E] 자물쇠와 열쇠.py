def rotate(a):
    row = len(a)
    col = len(a[0])
    res = [[0] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            res[c][row-1-r] = a[r][c]
    return res

def check(arr) :
    length = len(arr) // 3
    for i in range(length,length * 2):
        for j in range(length,length * 2):
            if arr[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)

    temp_lock = [[0] * (n * 3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            temp_lock[i+n][j+n] = lock[i][j]
            #정중앙에 기존 자물쇠
    for _ in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        temp_lock[x+i][y+j] += key[i][j]

                if check(temp_lock) :
                    return True
                for i in range(m):
                    for j in range(m):
                        temp_lock[x+i][y+j] -= key[i][j]
    return False

solution(key,lock)