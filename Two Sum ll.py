def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        l=0
        r=len(numbers)-1
        while len(ans)<2:
            if numbers[l]+numbers[r]==target:
                ans.append(l+1)
                ans.append(r+1)
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
        return ans
