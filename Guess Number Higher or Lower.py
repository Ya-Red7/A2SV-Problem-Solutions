class Solution:
    def guessNumber(self, n: int) -> int:
        s,e = 1,n
        while 1:
            m=(s+e)//2
            if guess(m)==0:
                return m
            elif guess(m)==-1:
                e=m-1
            else:
                s=m+1
