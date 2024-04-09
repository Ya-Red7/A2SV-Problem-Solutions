def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n= len(grid)-2
        ans=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[i][j]= max(grid[x][y] for x in range(i,i+3) for y in range(j,j+3))
        return ans
