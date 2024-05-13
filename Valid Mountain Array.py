def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        ml=-1
        mr=-1
        if n<3: return False
        i=1
        while i<n:
            if arr[i]==arr[i-1]:return False
            if arr[i]<arr[i-1]: 
                ml=i-1
                break
            i+=1
        i=n-1
        while i>0:
            if arr[i]==arr[i-1]: return False
            if arr[i-1]<arr[i]:
                mr=i
                break
            i-=1
        return mr==ml
