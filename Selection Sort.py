def select(self, arr, i):
        # code here 
        index=i
        for j in range(i+1,n):
            if arr[j]<arr[index]:
                index=j
        arr[index],arr[i] = arr[i],arr[index]
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            self.select(arr,i)
        return arr
