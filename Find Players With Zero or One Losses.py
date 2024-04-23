def findWinners(self, mat: List[List[int]]) -> List[List[int]]:
        hMap=defaultdict(int)
        for i in mat:
            hMap[i[0]]+=0
            hMap[i[1]]+=1
        winner = sorted([k for k,l in hMap.items() if l==0])
        loser = sorted([k for k,l in hMap.items() if l==1])
        return [winner,loser]
