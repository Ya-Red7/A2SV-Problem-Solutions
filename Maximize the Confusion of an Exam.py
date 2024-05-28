def maxConsecutiveAnswers(self, ak: str, k: int) -> int:
        ans=temp=mini=0
        i=j=0
        cntT=cntF=0
        while i<len(ak):
            if ak[i]=='T':
                cntT+=1
            else:
                cntF+=1
            i+=1
            temp+=1
            if cntT >k and cntF>k:
                
                while (cntT>k and cntF>k):
                    if ak[j]=='T':
                        cntT-=1
                    else:
                        cntF-=1
                    j+=1
                    temp-=1
            ans=max(ans,temp)
        return ans
