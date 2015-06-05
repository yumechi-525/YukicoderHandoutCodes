import math
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
	t = li[i][1] * math.log10(li[i][0])
	Z = int(t)
	f = t - Z
	X, Y = 0, 0
	for i in range(1, 11):
		if math.log10(i) > f:
			X = i-1
			break
	for j in range(0, 11):
		if j == 0:
			if math.log10(X) > f:
				break
		else:
			if math.log10(X + j / 10) > f:
				Y = j - 1
				break
	print(X, Y, Z)