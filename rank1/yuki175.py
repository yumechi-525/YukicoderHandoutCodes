l, n = int(input()), int(input())
sli = input().split()
res = 0
for s in sli:
    res += 2 ** (l - len(s))
print(res)
