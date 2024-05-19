def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tf=1
        n=len(nums)-1
        while tf:
            tf=0
            for i in range(n):
                if nums[i]==0 and nums[i+1]!=0:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    tf=1
        
