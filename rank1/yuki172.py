import math

x, y, r = map(int, input().split())
print(math.ceil(abs(x) + abs(y) + math.sqrt(2) * r))
