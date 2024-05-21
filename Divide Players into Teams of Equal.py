def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        totalSkill = skill[i]+skill[j]
        chem = 0
        while i<j:
            if skill[i]+skill[j] !=totalSkill:
                return -1
            else:
                chem+= skill[i]*skill[j]
            i+=1
            j-=1
        return chem
