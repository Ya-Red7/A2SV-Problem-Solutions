if __name__ == '__main__':
    N = int(input())
    ls = []
    for _ in range(N):
        temp = list((str, input().split()))
        if temp[1][0]=='print': print(ls)
        elif temp[1][0]=='sort': ls.sort()
        elif temp[1][0]=='pop': ls.pop()
        elif temp[1][0]=='reverse': ls.reverse()
        elif temp[1][0]=='remove': ls.remove(int(temp[1][1]))
        elif temp[1][0]=='insert': ls.insert(int(temp[1][1]), int(temp[1][2]))
        elif temp[1][0]=='append': ls.append(int(temp[1][1]))
        
