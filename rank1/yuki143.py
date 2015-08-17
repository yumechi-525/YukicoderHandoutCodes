k, n, f = map(int, input().split())
alis = list(map(int, input().split()))
res = k * n - sum(alis)
print(res if res >= 0 else -1)