import math

def solve():
	a, b = map(int, input().split())
	c = b / a
	print("NO" if c != math.ceil(c) else int(c))

if __name__=="__main__":
    solve()
