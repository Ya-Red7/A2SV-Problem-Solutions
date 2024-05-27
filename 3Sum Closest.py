def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curr=1000000
        for i in range(len(nums)-1):
            
            j=i+1
            k=len(nums)-1
            while j<k:
                if abs((nums[j]+nums[k]+nums[i])-target)<curr:
                    ans=nums[j]+nums[k]+nums[i]
                    curr=abs((nums[j]+nums[k]+nums[i])-target)
                
                if nums[j]+nums[k]+nums[i]>target:
                    k-=1
                else:
                    j+=1
                
        return ans
