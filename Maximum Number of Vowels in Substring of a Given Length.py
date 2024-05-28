def maxVowels(self, s: str, k: int) -> int:
        ans=temp=j=0
        vowels=['a','e','i','o','u']
        for i in range(len(s)):
            if i<k:
                if s[i] in vowels:
                    temp+=1
            else:
                if s[j] in vowels:
                    temp-=1
                if s[i] in vowels:
                    temp+=1
                j+=1
            ans=max(ans,temp)
            if ans==k: return k
        return ans
