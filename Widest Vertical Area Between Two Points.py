def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort()
        for i in range(1,len(points)):
            curr = points[i][0]-points[i-1][0]
            ans = max(curr,ans)
        return ans
