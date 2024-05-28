def lengthOfLongestSubstring(self, s: str) -> int:
        dictS={}
        for i in s:
            dictS[i]=0
        ans=temp=0
        i=j=0
        while i<len(s):
            dictS[s[i]]+=1
            if dictS[s[i]]<=1:
                i+=1
                temp+=1
                ans=max(temp,ans)
            else:
                while dictS[s[i]]>1:
                    dictS[s[j]]-=1
                    j+=1
                i+=1
                temp=i-j
        return max(temp,ans)
