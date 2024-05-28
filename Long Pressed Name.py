def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed): return 0
        i=j=0
        while i<len(name)-1 or j<len(typed)-1:
            if name[i]!=typed[j] or( i<len(name)-1 and j==len(typed)-1):
                return 0
            elif i!=len(name)-1:
                if name[i+1]==name[i] and typed[j+1]==typed[j] :
                    i+=1
                    j+=1
                elif name[i+1]!=name[i] and typed[j+1]==typed[j] :
                    j+=1
                else:
                    i+=1
                    j+=1
            elif i==len(name)-1:
                j+=1
        return name[i]==typed[j]
