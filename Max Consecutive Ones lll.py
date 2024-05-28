def longestOnes(self, nums: List[int], k: int) -> int:
        ans=temp=0
        i=j=0
        while i<len(nums):
            if nums[i]==1:
                temp+=1
                i+=1
                
            else:
                if k>0:
                    i+=1
                    temp+=1
                    k-=1
                else:
                    while k==0:
                        if nums[j]==0:
                            k+=1
                        temp-=1
                        j+=1
            ans=max(ans,temp)
        return max(ans,temp)
                        
