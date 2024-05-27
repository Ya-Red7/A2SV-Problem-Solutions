def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        ans=-1
        j=0
        for i in processorTime:
            temp = max(i+tasks[j],i+tasks[j+1],i+tasks[j+2],i+tasks[j+3])
            ans = max(ans,temp)
            j+=4
        return ans
