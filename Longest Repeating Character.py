def characterReplacement(self, s: str, k: int) -> int:
        alphs={}
        ans=0
        l=0
        for r in range(len(s)):
            alphs[s[r]] = 1 + alphs.get(s[r],0)
            while (r-l+1) - max(alphs.values()) > k:
                alphs[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
