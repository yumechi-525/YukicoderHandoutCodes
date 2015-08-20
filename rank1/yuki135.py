n = int(input())
xli = list(set(list(map(int, input().split()))))
xli.sort()
res = 10 ** 7
n = len(xli)
for i in range(n-1):
    res = min(res, xli[i+1] - xli[i])
print(res if res != 10 ** 7 else 0)
