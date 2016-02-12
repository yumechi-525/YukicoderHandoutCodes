import re

def solve():
    s = input()
    if s.count("ｗ") == 0 or s.count("ｗ") == len(s):
        print("")
        return True

    s = re.sub(r"^ｗ+", "", s)
    if s.count("ｗ") == 0:
        print("")
        return True
        
    removeW = re.sub(r"ｗ+", "ｗ", s)
    splitList = removeW.split("ｗ")
    matchwords = re.findall(r"ｗ+", s)
    maxW = max([len(c) for c in matchwords])
    idxlist = []
    for i in range(len(matchwords)):
        if len(matchwords[i]) == maxW:
            idxlist.append(i)
    idxlist.sort()
    print("\n".join([splitList[i] for i in idxlist]))
    return True

if __name__=="__main__":
    solve()