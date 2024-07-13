def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort(reverse=True)
        q = deque()
        for i in deck:
            if q:
                q.append(q.popleft())
            q.append(i)
        l, r = 0,len(q)-1
        ans = list(q)
        while l<r:
            ans[l],ans[r]=ans[r],ans[l]
            l+=1
            r-=1
        return ans
