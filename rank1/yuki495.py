import re

def solve():
	s = input()
	print("{0} {1}".format(len(re.findall(r"\(\^\^\*\)", s)), len(re.findall(r"\(\*\^\^\)", s))))


if __name__=="__main__":
    solve()
