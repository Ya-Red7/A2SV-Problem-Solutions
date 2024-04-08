def insertionSort1(n, arr):
    # Write your code here
    curr =arr[n-1]
    i=n-2
    while curr< arr[i]:
        arr[i+1]=arr[i]
        print(' '.join(map(str,arr)))
        arr[i]=curr
        if i==0:
            break
        i-=1
    print(' '.join(map(str,arr)))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
