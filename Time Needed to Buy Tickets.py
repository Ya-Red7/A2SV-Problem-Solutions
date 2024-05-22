def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        ans=0
        while t[k]!=0:
            for i in range(len(t)):
                if t[i]!=0: 
                    t[i]-=1
                    ans+=1
                if t[k]==0: break
        return ans
