def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0: nums[i]=0
            else: nums[i]=1

        l,curr,ans1=0,0,0
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>goal:
                curr-=nums[l]
                l+=1
            ans1+=(i-l+1)
        
        ans2,l,curr=0,0,0
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>goal-1:
                curr-=nums[l]
                l+=1
            ans2+=(i-l+1)
        return ans1-ans2
