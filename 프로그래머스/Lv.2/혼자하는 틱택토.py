from collections import deque

def check(board) :
    for b in board :
        if b != '...' :
            return False
    return True

def cnt(board,xTic,oTic) :
    xNum = 0
    oNum = 0
    for b in board :
        for sign in b :
            if sign == 'O' :
                oNum += 1
            elif sign == 'X' :
                xNum += 1
    return [oNum,xNum]

def tic(board, sign) :
    res = 0    
    for b in board :
        if b == sign*3 :
            res += 1
    for i in range(3) :
        if board[0][i] + board[1][i] + board[2][i] == sign * 3 :
            res += 1
    if board[0][0] + board[1][1] + board[2][2] == sign * 3:
        res += 1
    if board[0][2] + board[1][1] + board[2][0] == sign * 3 :
        res += 1
    return res
        
def solution(board):
    
    if check(board) :
        return 1
    xTic = tic(board,'X')
    oTic = tic(board,'O')
    
    # oTic은 2줄이 생길 수도 있음
    if oTic <= 1 and oTic + xTic > 1 :
        return 0
    
    oNum,xNum = cnt(board,xTic,oTic) 
    if oTic >= 1 and xNum+1 != oNum :
        # o Tic으로 끝났는데, 그 이후에 x를 놓은 경우
        return 0
    if xTic >= 1 and oNum != xNum :
        # x Tic으로 끝났는데, 그 이후 o를 놓은 경우
        return 0
    if xNum > oNum or oNum - xNum >= 2 :
        # X가 더 많거나, X 차례에 O를 함
        # 여기서, 끝났지만 개수를 다르게 놓은 경우가 다 걸러진덩
        return 0

    return 1
    