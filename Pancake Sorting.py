def pancakeSort(self, arr: List[int]) -> List[int]:
        tf=True
        n=len(arr)
        ans=[]
        while tf:

            ind=0
            for i in range(n):
                if arr[i]>arr[ind]:
                    ind=i
            if ind!=n-1:
                if ind!=0:

                    s=0
                    i=ind
                    while s<i:
                        arr[s],arr[i]=arr[i],arr[s]
                        s+=1
                        i-=1
                    ans.append(ind+1)
                s=0
                i=n-1
                while s<i:
                    arr[s],arr[i]=arr[i],arr[s]
                    s+=1
                    i-=1
                ans.append(n)
            n-=1
            if n<=1:
                tf=False
        return ans
