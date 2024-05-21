n ,m=map(int, input().split())
ans = []
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i=0
j=0
while i<n or j<m:
    if j==m or i<n and arr1[i]<arr2[j]:
        ans.append(arr1[i])
        i+=1
    else:
        ans.append(arr2[j])
        j+=1
print(*ans)
