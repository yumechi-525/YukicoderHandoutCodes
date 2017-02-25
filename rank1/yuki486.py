def solve():
	s = input()
	east_3win = s.find("OOO")
	west_3win = s.find("XXX")
	if east_3win >= 0 and west_3win >= 0:
		print("East" if east_3win < west_3win else "West")
	elif east_3win == -1 and west_3win >= 0:
		print("West")
	elif west_3win == -1 and east_3win >= 0:
		print("East")
	else:
		print("NA")

if __name__=="__main__":
    solve()
