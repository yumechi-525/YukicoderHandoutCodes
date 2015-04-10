__author__ = 'owner'
L = int(input())
N = int(input())
Wlist = list(map(int, input().split()))
Wlist.sort()
for i in range(N):
    if sum(Wlist[0:i + 1]) > L:
        print(i)
        break
else:
    print(N)