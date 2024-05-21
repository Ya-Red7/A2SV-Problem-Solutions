n ,m=map(int, input().split())
ans = []
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
j=0
cnt=0
for i in arr2:
    if j<n:
        if i>arr1[j] :
            while i>arr1[j]:
                j+=1
                #print(123)
                if j>=n: break
        ans.append(j)
    else :
        ans.append(j)
print(*ans)
