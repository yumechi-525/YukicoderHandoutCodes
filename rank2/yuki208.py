import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
diff = math.fabs(x1 - y1)
clac = lambda x, y: min(math.fabs(x), math.fabs(y))
res = diff + clac(x1, y1)

if diff == 0:
    if math.fabs(x2) == math.fabs(y2):
        if 0 < x2 < x1 and 0 < y2 < y1:
            res += 1
        elif 0 < x2 < x1 and y1 < y2 < 0:
            res += 1
        elif x1 < x2 < 0 and 0 < y2 < y1:
            res += 1
        elif x1 < x2 < 0 and y1 < y2 < 0:
            res += 1

print(int(res))