def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        s=n//3
        sum=0
        t=n-2
        while s>0:
            sum+=piles[t]
            t-=2
            s-=1
        return sum
