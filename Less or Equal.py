n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr.sort()
ans=0
if k==0:
    ans=arr[0]-1
else:
    ans=arr[k-1]
count=0
for i in range(len(arr)):
    if arr[i] <= ans: count+=1
if count!=k or not(1 <= ans and ans <= 1000 * 1000 * 1000):
    print(-1)
else:
    print(ans)
