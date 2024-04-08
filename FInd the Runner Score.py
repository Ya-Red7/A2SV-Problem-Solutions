if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2= list(arr)
    max= arr2[0]
    ans=0
    for i in arr2:
        if max< i:
            ans=max
            max=i
        elif ans<i and i!=max:
            ans=i
    print(ans)
