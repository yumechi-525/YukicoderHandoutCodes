from collections import defaultdict
import itertools


def solve():
	n, m = map(int, input().split())
	node_pair = []
	
	for _ in range(m):
		a, b = map(int, input().split())
		node_pair.append([a, b])
	
	node_dict = defaultdict(list)
	for pair in node_pair:
		node_dict[pair[0]].append(pair[1])
		node_dict[pair[1]].append(pair[0])
	
	ans = 0
	for square in list(itertools.combinations(range(0, n+1), 4)):
		for idx in range(4):
			connection_count = 0
			for node in node_dict[square[idx]]:
				if node in square:
					connection_count += 1
			if connection_count != 2:
				break
		else:
			ans += 1
	print(ans)


if __name__=="__main__":
    solve()
