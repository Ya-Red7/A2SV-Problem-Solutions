def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1,count2,count3=(0,0,0)
        for i in range(len(nums)):
            if nums[i]==0:
                count1+=1
            elif nums[i]==1:
                count2+=1
            else:
                count3+=1
        i=0
        while count1>0:
            nums[i]=0
            i+=1
            count1-=1
        while count2>0:
            nums[i]=1
            i+=1
            count2-=1
        while count3>0:
            nums[i]=2
            i+=1
            count3-=1
