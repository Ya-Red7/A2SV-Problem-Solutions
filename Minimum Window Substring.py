def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t == "": return ""
        dictT , dictS = Counter(t), {}
        ind , minLen = [-1,-1], float("infinity")
        l , have , need = 0 , 0 , len(dictT)
        for r in range(len(s)):
            ch = s[r]
            dictS[ch] = 1 + dictS.get(ch,0)
            if ch in dictT and dictS[ch] == dictT[ch]:
                have+=1
            while  have == need:
                if minLen > r - l + 1:
                    ind = [l,r]
                    minLen = r - l + 1
                dictS[s[l]]-=1
                if s[l] in dictT and dictS[s[l]] < dictT[s[l]]:
                    have-=1
                l+=1
        if minLen == float("infinity"):
            return ""
        l,r = ind
        return s[l:r+1]
