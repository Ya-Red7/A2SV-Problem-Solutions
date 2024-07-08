def scoreOfParentheses(self, s: str) -> int:
        curr=0
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(curr)
                curr=0
            else:
                curr += stack.pop()+max(curr,1)
        return curr
