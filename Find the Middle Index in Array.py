def findMiddleIndex(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            if i==len(nums)-1 and s!=0 : return -1
            elif i==len(nums)-1 and s==0 : return i
            cs = sum(nums[i+1:])
            if s==cs: return i
            s+=nums[i]
        return -1
