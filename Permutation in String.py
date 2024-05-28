def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        for i in range(len(s2)-n+1):
            x=0
            j=i
            temp=""
            while x<n:
                temp+=s2[j]
                x+=1
                j+=1
            tf=1
            if sorted(temp)==sorted(s1): return True
        return False
