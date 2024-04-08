def similarPairs(self, words: List[str]) -> int:
        word_sorted = [sorted(set(x)) for x in words]
        ans=0
        n= len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                if word_sorted[i]==word_sorted[j]:
                    ans+=1
        return ans
