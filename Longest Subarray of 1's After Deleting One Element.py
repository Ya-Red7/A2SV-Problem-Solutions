def longestSubarray(self, nums: List[int]) -> int:
        ans=temp=0
        i=j=0
        zero = 1
        while i<len(nums):
            if nums[i]==1:
                i+=1
                temp+=1
                ans=max(temp,ans)
            else:
                if zero!=0:
                    zero-=1
                    i+=1
                else:
                    while zero==0:
                        if nums[j]==0:
                            zero+=1
                        j+=1
                    temp=i-j
        ans=max(ans,temp)
        if ans==len(nums): ans-=1
        return ans
