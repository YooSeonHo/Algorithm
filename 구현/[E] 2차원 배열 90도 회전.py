def rotate_arr(a):
    row = len(a)
    col = len(a[0])
    res = [[0] * row for _ in range(col)]

    for r in range(row):
        for c in range(col) :
            res[c][row -1 - r] = a[r][c]
            #회전 후 행번호 = 회전 전 열번호(c)
            #회전 후 열번호 = row# - 1 - 회전 전 행번호 (index가 0부터 시작하니까 1 빼주는거)
    return res

#90도 회전하면 행과 열이 반대가 된다는 것을 기억!

def rotate_arr2(a):
    rotated = list(zip(*a[::-1]))
    #리스트를 역순으로 뒤집어서 zip
    #자료형은 [(),()] 튜플로 바뀜..