class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            cnt = 0
            indx = i
            visited = []
            while len(visited)<=n:
                visited.append(nums[indx])
                togo = indx+nums[indx]
                togo%=n
                if abs(nums[indx])==n or nums[i]*nums[indx]<0 or (togo==indx):
                    break
                if indx==i and cnt>0:
                    return True
                indx=togo
                cnt+=1
        return False
