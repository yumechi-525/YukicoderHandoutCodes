N = int(input())
allset = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for _ in range(N):
    l = input().split()
    for i in range(4):
        l[i] = int(l[i])
    s = set(l)
    if l[4] == "YES":
        allset = allset & s
    else:
        allset = allset - s
    if len(allset) == 1:
        print(allset.pop())
        break
