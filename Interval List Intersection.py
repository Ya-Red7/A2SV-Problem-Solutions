def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        j=i=0
        ans=[]
        while i<len(firstList) and j<len(secondList):
            if firstList[i][1]<secondList[j][0]:
                i+=1
                continue
            if firstList[i][0]<=secondList[j][0]:
                if firstList[i][1]<=secondList[j][1]:
                    ans.append([secondList[j][0],firstList[i][1]])
                    i+=1
                else:
                    ans.append([secondList[j][0],secondList[j][1]])
                    j+=1
            elif firstList[i][0]<=secondList[j][1]:
                if firstList[i][1]<=secondList[j][1]:
                    ans.append([firstList[i][0],firstList[i][1]])
                    i+=1
                else:
                    ans.append([firstList[i][0],secondList[j][1]])
                    j+=1
            elif firstList[i][0]>secondList[j][1]:
                j+=1
        return ans
