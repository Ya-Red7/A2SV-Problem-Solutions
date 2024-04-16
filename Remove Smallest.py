n=int(input())
for i in range(n):
    n2=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    tf=True
    for i in range(n2-1):
        if arr[i+1]-arr[i]!=0 and arr[i+1]-arr[i]!=1:
            tf=False
            break
    if tf: print("YES")
    else: print("NO")
