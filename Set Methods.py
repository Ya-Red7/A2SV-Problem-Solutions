# Enter your code here. Read input from STDIN. Print output to STDOUT
sa = set(map(int, input().split()))
n = int(input())
for i in range(n):
    tempset = set(map(int, input().split()))
    dif = sa - tempset
    if not (dif and sa.issuperset(tempset)):
        print(False)
        quit()
print(True)
