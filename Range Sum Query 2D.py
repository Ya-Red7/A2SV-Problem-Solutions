class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        col = len(matrix[0])+1
        row = len(matrix)+1
        self.ls = [[0]*col for _ in range(row)]
        for i in range(1,row):
            for j in range(1,col):
                
                self.ls[i][j] =( matrix[i-1][j-1])+(self.ls[i-1][j])+(self.ls[i][j-1])-(self.ls[i-1][j-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tl ,tr ,bl, br= [row1+1,col1+1], [row1+1,col2+1], [row2+1,col1+1], [row2+1,col2+1]
        return self.ls[br[0]][br[1]] - self.ls[bl[0]][bl[1]-1] - self.ls[tr[0]-1][tr[1]] + self.ls[tl[0]-1][tl[1]-1]
