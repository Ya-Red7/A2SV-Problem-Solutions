def reductionOperations(self, nums: List[int]) -> int: 
        nums.sort()
        ans=0
        n =0
        curr=1
        #if len(nums)==1: return ans
        for i in range(len(nums)):
            if nums[i]==nums[0]: continue
            if nums[i]==curr:
                ans+=n
            else:
                curr=nums[i]
                n+=1
                ans+=n
        return ans
