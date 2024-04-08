#Longest Common Prefix
def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        strs.sort(key=len)
        m= len(strs[0])
        pre=""
        for i in range(m):
            for j in range(n):
                if strs[0][i]!=strs[j][i]:
                    return pre
            pre+= strs[0][i]
        return pre
