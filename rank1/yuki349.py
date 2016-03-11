from collections import Counter
n = int(input())
c = Counter([input() for _ in range(n)])
print("YES" if (n+1)//2>=max(c.values()) else "NO")
