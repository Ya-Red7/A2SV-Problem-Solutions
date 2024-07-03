def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n<5: return 0
        nums.sort()
        ans = float("inf")
        for i in range(4):
            ans = min(ans,nums[n-4+i]-nums[i])
        return ans
