def numTimesAllBlue(self, flips: List[int]) -> int:
        ans=0
        s=0
        s2=0
        for i in range(len(flips)):
            s+=i+1
            s2+=flips[i]
            if s==s2: ans+=1
        return ans
