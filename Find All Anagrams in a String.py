def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        np=len(p)
        if len(s)<np: return ans
        dictP = Counter(p)
        for i in range(len(s)-np+1):
            if Counter(s[i:i+np])==dictP:
                ans.append(i)
        return ans
