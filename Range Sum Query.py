class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preSum = [0]*(len(self.nums)+1)


    def sumRange(self, left: int, right: int) -> int:
        for i in range(len(self.nums)):
            self.preSum[i+1] = (self.preSum[i]+self.nums[i])
        r = right+1
        l = left+1
        return self.preSum[r] - self.preSum[l-1]
