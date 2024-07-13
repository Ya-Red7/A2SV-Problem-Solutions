class MinStack:

    def __init__(self):
        self.stack = []
        self.minim = float("inf")

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append([val,self.minim])
            self.minim = min(self.stack[-1][1],val)
            
        else:
            self.stack.append([val,val])
            self.minim = val
    def pop(self) -> None:
        temp = self.stack.pop()
        if temp[0]==self.minim:
            self.minim = temp[1]
        
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minim


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
