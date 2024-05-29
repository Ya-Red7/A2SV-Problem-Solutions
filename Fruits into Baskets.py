def totalFruit(self, fruits: List[int]) -> int:
        dictN={}
        for i in fruits:
            dictN[i]=0
        l=0
        n=ans=0
        for r in range(len(fruits)):
            dictN[fruits[r]]+=1
            if dictN[fruits[r]]==1: n+=1
            while n>2:
                dictN[fruits[l]]-=1
                if dictN[fruits[l]]==0: n-=1
                l+=1
            ans=max(ans,(r-l+1)) 
        return ans
