class Solution:
    def freqAlphabets(self, s: str) -> str:
        n=len(s)-1
        ans=""
        while(n>=0):
            if s[n]=='#':
                temp= int(s[n-2])*10 + int(s[n-1])
                temp_char = chr(temp+96)
                ans = temp_char + ans
                n-=2
            else:
                temp= int(s[n])
                temp_char = chr(temp+96) 
                ans = temp_char + ans
            n-=1
        return ans
