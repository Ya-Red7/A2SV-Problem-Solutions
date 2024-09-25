class Solution:
    def minSteps(self, n: int) -> int:
        def prime(n):
            cnt = 0
            while n%2==0:
                cnt+=2
                n//=2
            for i in range(3,int(sqrt(n))+1,2):
                while n%i==0:
                    cnt+=i
                    n//=i
            if n>2:
                cnt+=n
            return cnt
        return prime(n)
