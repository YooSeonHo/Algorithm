n = int(input())

# 2 -> 5 
# 3 -> 9 = 5 + 4
# 4 -> 13 = 9 + 4
#1,2 , -1,-2 번째 줄마다 추가해야함 

s = []
def star(n) :
    if n == 2 :
        s.append('*****')
        s.append('*')
        s.append('* ***')
        s.append('* * *')
        s.append('* * *')
        s.append('*   *')
        s.append('*****')
        return
    else :
        star(n-1)
        start = len(s[0])
        s.insert(0,'*' * (start+4))
        s.insert(1,'*')
        for i in range(2,len(s)) :
            s[i] = '* ' + s[i]
            
            while len(s[i]) <= start + 2 : 
                if i == 2 :
                    s[i] = s[i] + '*'
                else :
                    s[i] = s[i] + ' '
            s[i] = s[i] + '*'
        s.insert(len(s),'*' * (start+4))
        s.insert(len(s)-1,'*' + ' ' * (start+2) + '*')


if n == 1:
    print('*')
else :
    star(n)
    print(*s,sep='\n')
