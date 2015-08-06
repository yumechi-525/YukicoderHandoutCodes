n = int(input())
for i in range(n):
  g, d = map(int, input().split())
  s = g - 30000 * d
  if s * 6 >= 3000000:
    print("YES")
    for _ in range(6):
      print(i+1)
    exit(0)
print("NO")
