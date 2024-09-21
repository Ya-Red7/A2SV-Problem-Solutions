class Solution:
    def findGCD(self, nums: List[int]) -> int:
        sm = lg = nums[0]
        for i in nums:
            if i<sm: sm = i
            if i>lg: lg = i
        def hcfnaive(a, b):
            if(b == 0):
                return abs(a)
            else:
                return hcfnaive(b, a % b)
        return hcfnaive(sm,lg)
