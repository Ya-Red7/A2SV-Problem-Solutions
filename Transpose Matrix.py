def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix[0])
        n = len(matrix)
        ans = [[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i]= matrix[i][j]
        return ans
