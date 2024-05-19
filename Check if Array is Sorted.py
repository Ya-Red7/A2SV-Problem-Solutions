def arraySortedOrNot(self, arr, n):
        # code here
        if n==1: return 1
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                return 0
        return 1
