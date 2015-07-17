import sys

res = -1
low, high = 1, 10 ** 9
check = []
for i in range(100):
	mid = (low + high) // 2
	if mid in check:
		print("!", mid)
		sys.stdout.flush()
		break
	check.append(mid)
	print("?", mid)
	sys.stdout.flush()
	res = int(input())
	if res == 1:
		low = mid
	else:
		high = mid
