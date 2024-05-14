def smallestNumber(self, num: int) -> int:
        if num==0:return 0
        snum = str(num)
        ls = []
        tf=0
        
        for i in range(len(snum)):
            if snum[i] =='-':
                tf=1
                continue
            ls.append(snum[i])
        if tf:
            
            ls.sort(reverse=True)
            temp = ''.join(ls)
            temp = '-'+temp
            return int(temp)
        else:
            ls.sort()
            i=0
            while ls[i]=='0' and i<len(ls):
                i+=1
            ls[0],ls[i]=ls[i],ls[0]
            return int(''.join(ls))
