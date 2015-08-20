p, q = map(float, input().split())
print("YES" if q * (1 - p) < p * q * (1 - q) else "NO")