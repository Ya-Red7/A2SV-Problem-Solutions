#Concatenation of Array
def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
