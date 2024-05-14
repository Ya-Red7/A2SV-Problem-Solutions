def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr2)):
            while 1:
                try:
                    arr1.remove(arr2[i])
                    ans.append(arr2[i])
                except:
                    break
        if arr1:
            arr1.sort()
            for i in arr1:
                ans.append(i)
        return ans
