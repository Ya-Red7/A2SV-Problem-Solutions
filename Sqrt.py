class Solution:
    def mySqrt(self, x: int) -> int:
        s,e = 0,x
        while 1:
            n = (s+e)//2
            if n*n==x:
                return n
            elif n*n<x:
                if (n+1)*(n+1)>x: return n
                s = n+1
            else:
                if (n+1)*(n+1)<x: return n
                e = n-1
