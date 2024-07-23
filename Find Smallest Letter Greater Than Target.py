class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target>=letters[-1]:
            return letters[0]
        s,e = 0,len(letters)-1
        while 1:
            m = (s+e)//2
            if letters[m]<=target:
                if letters[m+1]>target: return letters[m+1]
                s=m+1
            elif letters[m]>=target:
                if letters[m+1]<target: return letters[m]
                e=m-1
