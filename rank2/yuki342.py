import re

def solve():
    s = re.sub(r"^ｗ+", "", input())
    if s.count("ｗ") == 0:
        print("")
        exit(0)
 
    removeW = re.sub(r"ｗ+", "ｗ", s)
    splitList = removeW.split("ｗ")
    matchwords = re.findall(r"ｗ+", s)
    maxW = max([len(c) for c in matchwords])
    idxlist = [i for i in range(len(matchwords)) if len(matchwords[i]) == maxW]
    print("\n".join([splitList[i] for i in idxlist]))

if __name__=="__main__":
    solve()