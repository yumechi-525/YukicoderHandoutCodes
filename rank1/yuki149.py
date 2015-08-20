aw, ab = map(int, input().split())
bw, bb = map(int, input().split())
c, d = map(int, input().split())

if c > ab:
    aw -= c - ab
    bw += c - ab

print(aw + d if d <= bw else aw + bw)