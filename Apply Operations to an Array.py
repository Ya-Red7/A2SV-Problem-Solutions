def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i]=0
                nums[i-1] *= 2
        tf= True
        while tf :
            tf=False
            for i in range(len(nums)-1):
                if nums[i]==0:
                    if nums[i+1]!=0:
                        nums[i],nums[i+1]=nums[i+1],nums[i]
                        tf=True
        return nums
