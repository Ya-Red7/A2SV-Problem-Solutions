def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr = []
        currSum=0
        for n in nums:
            currSum+=n
            rem = currSum%k
            if rem<0: remp+=k
            arr.append(rem)
        cnt = 0
        map={0:1}
        for i in range(len(arr)):
            pre = map.get(arr[i],-1)
            if arr[i] in map:
                cnt+= map[arr[i]]
                map[arr[i]]+=1
            else:
                map[arr[i]]=1
                
        return cnt
