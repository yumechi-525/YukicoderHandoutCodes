l, k = map(int, input().split())
l = l - l % (k * 2) if l % (k * 2) != 0 else l - k * 2
print(l // 2)
