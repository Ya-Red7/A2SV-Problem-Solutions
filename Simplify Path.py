def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for i in arr:
            if i == '..':
                if stack:
                    stack.pop()
            elif i != '.' and i != "":
                stack.append(i)
        return '/' + '/'.join(stack)
