def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''di = {}
        for i in range(len(points)):
            temp = ((points[i][0] ** 2) + (points[i][1] ** 2)) ** 0.5
            di[temp] = points[i]
        di = dict(sorted(di.items()))
        ls = list(di.values())
        n = len(points) - 1
        ans = ls[:k]'''
        points.sort(key = lambda x: ((x[0] ** 2) + (x[1] ** 2)) ** 0.5)
        
        return points [:k]
