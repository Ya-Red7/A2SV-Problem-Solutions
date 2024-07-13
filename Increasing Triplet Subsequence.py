def increasingTriplet(self, nums: List[int]) -> bool:
        small,large = [],[0]*len(nums)
        #minim,maxim = float("-inf"),float("inf")
        for i in nums:
            if small:
                small.append(minim)
                minim = min(i,minim)
            else:
                small.append(i)
                minim = i
        for i in range(len(nums)-1,-1,-1):
            if large:
                large[i]=(minim)
                minim = max(nums[i],minim)
            else:
                large[i]=(nums[i])
                minim = nums[i]
        print(*small,*large)
        for i in range(1,len(nums)-1):
            if small[i]<nums[i] and large[i]>nums[i]:
                return True
        return False
