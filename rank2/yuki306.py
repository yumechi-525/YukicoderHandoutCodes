import math as m

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
funcdiff = lambda x, y1, y2: m.sqrt(x ** 2 + abs(y1 - y2) ** 2)
low = 0.0
high = 1000.0
lowdiff =  funcdiff(x1, low, y1) + funcdiff(x2, low, y2)
highdiff =  funcdiff(x1, high, y1) + funcdiff(x2, high, y2)
while True:
    middiff = (lowdiff + highdiff) // 2
    mid = (low + high) // 2
    if low >= high:
        break
    print(lowdiff, highdiff, middiff, mid)
    if abs(middiff - lowdiff) > abs(highdiff - middiff):
        low = mid
    else:
        high = mid
    lowdiff =  funcdiff(x1, low, y1) + funcdiff(x2, low, y2)
    highdiff =  funcdiff(x1, high, y1) + funcdiff(x2, high, y2)
print(low)