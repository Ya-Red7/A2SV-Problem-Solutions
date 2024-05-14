def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(heights)):
            dic[heights[i]] = names[i]
            keysl = list(dic.keys())
            keysl.sort(reverse=True)
            sorted_dict = []
        for i in range(len(heights)):
            sorted_dict.append(dic[keysl[i]])
        return sorted_dict
