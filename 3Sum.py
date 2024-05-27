def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-1):
            op = 0-nums[i]
            j=i+1
            k=len(nums)-1
            if i!=0:
                if nums[i]==nums[i-1]:
                    continue
            
            while j<k:
                if j!=i+1:
                    if nums[j]==nums[j-1]:
                        j+=1
                        continue
                if k!=len(nums)-1:
                    if nums[k]==nums[k+1]:
                        k-=1
                        continue
                if nums[j]+nums[k]==op:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]>op:
                    k-=1
                else:
                    j+=1
        return ans
