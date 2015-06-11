f0, f1, n = map(int, input().split())
if n % 3 == 0:
	print(f0)
elif n % 3 == 1:
	print(f1)
else:
	print(f0^f1)