class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target <= nums[0]:
            return 0
        if target>nums[-1]:
            return n
        
        s,e = 0,n-1
        while 1:
            m = (s+e)//2
            if nums[m]<=target:
                if nums[m]==target:
                    return m
                if nums[m+1]>target: return m+1
                s=m+1
            elif nums[m]>=target:
                if nums[m]==target:
                    return m
                if nums[m+1]<target: return m
                e=m-1
