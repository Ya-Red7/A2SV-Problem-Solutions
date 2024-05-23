def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans=0
        for i in range(left,right+1):
            for s,e in ranges:
                if i in [s for s in range(s,e+1)]:
                    ans+=1
                    break
        return ans==right-left+1
