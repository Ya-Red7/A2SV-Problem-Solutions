def minimumRecolors(self, blocks: str, k: int) -> int:
        ans, cntb,cntw,l=10000,0,0,0
        for i in range(len(blocks)):
            if blocks[i]=='B': cntb+=1
            else: cntw+=1
            if i>=k:
                if blocks[l]=='B': cntb-=1
                else: cntw-=1
                l+=1
            if cntb+cntw>=k:
                ans = min(ans,cntw)
        return ans
