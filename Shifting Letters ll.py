def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*(n+1)
        for st, e, d in shifts:
            if d == 1:
                arr[st]+=d
                arr[e+1]-=d
            else:
                arr[st]-=1
                arr[e+1]+=1
        for i in range(1,n+1):
            arr[i]=arr[i]+arr[i-1]
        
        k = ord('a')
        ans=''
        for i in range(n):
            num = arr[i]%26
            ans+= chr((ord(s[i]) - k + num  +26)%26 + k)
        return ans
