def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        ans=0
        x=0
        ind=0
        for i in range(len(nums)):
            sum+=nums[i]
            x+=1
            if sum>=target:
                if ans==0: ans=1000000
                
                while sum>=target:
                    ans=min(x,ans)
                    sum-=nums[ind]
                    ind+=1
                    x-=1
        return ans
