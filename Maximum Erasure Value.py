def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dictN = {}
        ans , l , sum = -1 , 0 , 0

        for r  in range(len(nums)):
            ch = nums[r]
            dictN[ch] = 1 + dictN.get(ch,0)
            while dictN[ch] > 1:
                sum-=nums[l]
                dictN[nums[l]]-=1
                l+=1
            sum+=ch
            ans = max(ans,sum)
        return ans
