def minimumCardPickup(self, cards: List[int]) -> int:
        dictN = {}
        ans , curr = float("infinity"),0
        for i in range(len(cards)):
            if cards[i] in dictN:
                curr = i - dictN[cards[i]] + 1
                ans = min(ans,curr)
            dictN[cards[i]] = i
        if ans == float("infinity"):
            return -1
        return ans
