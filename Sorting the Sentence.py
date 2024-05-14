def sortSentence(self, s: str) -> str:
        ls = s.split()
        di = {}
        for i in ls:
            di[i[-1]] = i[:-1]
        di2 = dict(sorted(di.items()))
        return ' '.join(list(di2.values()))
