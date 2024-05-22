def isValid(self, s: str) -> bool:
        stack =[]
        paren = {"(":")","[":"]","{":"}"}
        for i in range(len(s)):
            if s[i] in paren.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                x = stack.pop()
                if paren[x]!=s[i]:
                    return False
        return stack==[]
