def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        di = {'+':add,'-':sub,'*':mul,'/':truediv}
        for i in range (len(tokens)):
            if tokens[i] in di:
                stack[-1] = int(di[tokens[i]](stack[-2],stack.pop()))
            else:
                stack.append(int(tokens[i]))
        return int(stack.pop())
