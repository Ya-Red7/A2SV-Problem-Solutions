def rotate(self, mx: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mx)//2
        x=0
        y=len(mx)-1
        while n:
            t=0
            for i in range(x,y):
                temp= mx[i][y]
                mx[i][y]=mx[x][i]
                temp2=mx[y][y-t]
                mx[y][y-t]=temp
                mx[x][i]=mx[y-t][x]
                mx[y-t][x]=temp2
                t+=1
            x+=1
            y-=1
            n-=1
