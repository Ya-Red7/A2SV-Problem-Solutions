def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        coldict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        boxdict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        y=0
        x=0
        temp=0
        temp2=0
        k=1
        for i in range(9):
            if i//3==k and i!=0:
                temp2+=3
                y=temp2
                x=0
                temp=0
                k+=1
            l=1
            for j in range(9):
                if j//3==l and j!=0:
                    y+=1
                    x=temp
                    l+=1
                if board[i][j]!='.':
                    rowdict[board[i][j]]+=1
                    if rowdict[board[i][j]]>1:
                        return False
                if board[j][i]!='.':
                    coldict[board[j][i]]+=1
                    if coldict[board[j][i]]>1:
                        return False 
                print(y,x)
                if board[y][x]!='.':
                    boxdict[board[y][x]]+=1
                    if boxdict[board[y][x]]>1:
                        return False
                x+=1
            y=temp2
            temp+=3
            
            rowdict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            coldict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            boxdict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        return True
