N = int(input())
moneys = list(map(int, input().split()))
th = sum(moneys) / 10
res = 0
for i in range(N):
    res += 30 if th >= moneys[i] else 0
print(res)