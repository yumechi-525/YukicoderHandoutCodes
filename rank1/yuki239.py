n = int(input())
renchon = "nyanpass"
tab = [0 for _ in range(n)]
for _ in range(n):
    sli = input().split()
    for i in range(n):
        if sli[i] == renchon:
            tab[i] += 1

mn = max(tab)
print((tab.index(mn) + 1) if tab.count(mn) == 1 and mn == n - 1 else -1)
