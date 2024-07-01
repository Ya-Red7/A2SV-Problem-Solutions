def productExceptSelf(self, nums: List[int]) -> List[int]:
        front , back= [0]*len(nums),[0]*len(nums)
        front[0],back[-1] = nums[0],nums[-1]
        j=len(nums)-2
        for i in range(1,len(nums)):
            front[i] = front[i-1]*nums[i]
            back[j] = back[j+1]*nums[j]
            j-=1
        ans = [0]*len(nums)
        
        for i in range(len(nums)):
            if i==0:
                ans[i]= back[i+1]
            elif i==len(nums)-1:
                ans[i] = front[i-1]
            else:
                ans[i] = front[i-1]*back[i+1]
        return ans
