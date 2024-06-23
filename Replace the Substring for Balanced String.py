def balancedString(self, s: str) -> int:
        di = Counter(s)
        
        if di['Q']==di['W'] and di['E']==di['W'] and di['R']==di['E']:
            return 0
        beletu={}
        for k,v in di.items():
            if v > len(s)//4:
                beletu[k]=di[k]-len(s)//4
        
        l , have = 0, len(beletu)
        ans = float("infinity")
        for r in range(len(s)):
            ch = s[r]
            if ch in beletu:
                beletu[ch]-=1
                if beletu[ch]==0:
                    have-=1
            while have == 0:
                ans = min(ans, r-l+1)
                if s[l] in beletu:
                    beletu[s[l]]+=1
                    if beletu[s[l]] > 0 :
                        have+=1
                l+=1
        return ans
