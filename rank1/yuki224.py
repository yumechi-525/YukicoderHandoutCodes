n, s, t = int(input()), input(), input()
res = 0
for sc, tc in zip(s, t):
	if sc != tc:
		res += 1
print(res)