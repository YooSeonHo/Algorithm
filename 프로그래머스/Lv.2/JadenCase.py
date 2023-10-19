def solution(s):
    string = list(s.split(" "))
    res = []
    for st in string :
        if st == "" :
            res.append("")
        
        else :
            st = st[0].upper() + st[1:].lower()
            res.append(st)

    return ' '.join(map(str,res))