from collections import Counter
c=Counter(input())
d=Counter(c.values())
print((d[2]==6 and d[1]==1) and [e[0] for e in c.items() if e[1]==1][0] or "Impossible")
