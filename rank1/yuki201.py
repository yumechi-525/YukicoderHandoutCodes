sa, pa, xa = map(int, input().split())
sb, pb, xb = map(int, input().split())
if pa == pb:
	print(-1)
else:
	print(sa if pa > pb else sb)