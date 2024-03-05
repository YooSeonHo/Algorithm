from collections import defaultdict

def solution(genres, plays):
    res = []
    playCnt = defaultdict(int)
    genreIdx = defaultdict(list)
    n = len(plays)
    
    for i in range(n) :
        playCnt[genres[i]] += plays[i]
        genreIdx[genres[i]].append([i,plays[i]])
                
    sortCnt = list(sorted(playCnt.items(), key = lambda x : -x[1] ))
    
    for s in sortCnt :
        nowGenre = s[0]
        genreIdx[nowGenre].sort(key = lambda x: -x[1])
        
        for cnt in range(len(genreIdx[nowGenre])) :
            if cnt == 2:
                break
            res.append(genreIdx[nowGenre][cnt][0])
            
    return (res)