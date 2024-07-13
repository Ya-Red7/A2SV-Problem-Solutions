def dailyTemperatures(self, tem: List[int]) -> List[int]:
        stack,ans = [[tem[0],0]],[0]*len(tem)
        
        for i in range(1,len(tem)):
            while stack and stack[-1][0]<tem[i]:
                ans[stack[-1][1]] =i- stack[-1][1]
                stack.pop()
                
            stack.append([tem[i],i])
        return ans
