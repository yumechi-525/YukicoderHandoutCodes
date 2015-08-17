n, m = map(int, input().split())
candies = list(map(int, input().split()))
res, cur = 0, 0
while cur < m:
    cur += min(candies)
    if cur == m:
        res += 1
    if cur >= m:
        break
    res += 1
    candies.remove(min(candies))
print(res)