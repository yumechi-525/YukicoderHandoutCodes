import re

def solve():
    matchwords = re.findall(r"…+", input())
    matchwords.append("") # if no match pattern
    print(max([len(s) for s in matchwords]))

if __name__=="__main__":
    solve()