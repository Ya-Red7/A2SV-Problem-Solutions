#Goal Parser Interpratation
def interpret(self, str2: str) -> str:
        ans=""
        n=len(str2)
        i=0
        while(i<n):
            if str2[i]=='G':
                ans+='G'
            elif str2[i]=='(' and str2[i+1]==')':
                ans+='o'
                i=i+1
            else:
                ans+="al"
                i=i+3
            i=i+1
        return ans
