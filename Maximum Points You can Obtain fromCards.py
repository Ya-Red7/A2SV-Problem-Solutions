def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)
        
        if k == len(cardPoints):
            return totalSum
        n = len(cardPoints)-k
        
        l, minSum, currSum = 0, float("infinity"), sum(cardPoints[0:n])
        for r in range(n,n+k):
            minSum = min(minSum,currSum)
            currSum-=cardPoints[l]
            currSum+=cardPoints[r]
            l+=1
        return totalSum - min(minSum,currSum)
