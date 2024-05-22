def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return 0
        while n>=1:
            if n==1: return 1
            elif n%3==0: n//=3
            else: return 0
