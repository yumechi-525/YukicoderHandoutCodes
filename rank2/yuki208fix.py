x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
res = max(x1, y1)

if x1 == y1 and x2 == y2 and x2 < x1:
    res += 1
print(int(res))