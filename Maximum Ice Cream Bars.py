def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins<costs[0]: return 0
        i=0
        ans=0
        while coins and i<len(costs):
            coins-=costs[i]
            if coins<0: break
            ans+=1
            i+=1
        return ans
