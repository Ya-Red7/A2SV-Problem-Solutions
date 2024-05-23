from collections import defaultdict
n,m = map(int,input().split())
di = defaultdict(list)
for i in range(1,n+1):
    temp=input()
    di[temp].append(i)
for _ in range(m):
    temp=input()
    if temp in di:
        print(' '.join(map(str,di[temp])))
    else: print("-1")
