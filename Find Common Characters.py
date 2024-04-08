def commonChars(self, wor: List[str]) -> List[str]:
        ans=[]
        words = [sorted(z) for z in wor]
        curr = words[0]
        for x in curr:
            tf=True
            for i in range(1,len(words)):
                if x not in words[i]:
                    tf=False
                    break
                else:
                    words[i].remove(x)
            if tf:
                ans.append(x)
        return ans
