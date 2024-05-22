def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        init = [1]
        while rowIndex >0:
            temp=[]
            for i in range(len(init)):
                if i==0: temp.append(init[i])
                if i==len(init)-1: temp.append(init[i])
                if i+1<=len(init)-1:  temp.append(init[i]+init[i+1])
            init = temp
            rowIndex-=1
        return init
