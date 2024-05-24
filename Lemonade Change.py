def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0,10:0,20:0}
        
        for i in bills:
            if i==5:
                changes[5]+=1
            elif i==10:
                if changes[5]<=0: return False
                else:
                    changes[10]+=1
                    changes[5]-=1
            else:
                if changes[10]>0 and changes[5]>0:
                    changes[20]+=1
                    changes[5]-=1
                    changes[10]-=1
                elif changes[5]>=3:
                    changes[20]+=1
                    changes[5]-=3
                else: return False
        return True
