class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def hcfnaive(a, b):
            if(b == 0):
                return abs(a)
            else:
                return hcfnaive(b, a % b)
        if len(nums)==1 and k!=nums[0]: return 0




        cnt,i = 0,0
        while i<len(nums):
            if nums[i]==k: cnt+=1
            j = i+1
            gcd = None
            while i<len(nums)-1 and nums[i]%k==0 and j<len(nums):
                temp = hcfnaive(nums[j-1],nums[j])
                if temp!=k and (gcd is None or gcd==temp) and nums[j]%k==0:
                    gcd = temp
                    j+=1
                    continue
                elif nums[j]%k==0:
                    cnt+=1
                else:
                    break
                gcd = temp
                j+=1
            i+=1
        return cnt
