gi, ci, pi = map(int, input().split())
s = list(input())
gc, cc, pc = s.count("G"), s.count("C"), s.count("P")
res = 0

# win count
res += cc * 3 if gi > cc else gi * 3
gi, cc = gi - cc if gi >= cc else 0, cc - gi if cc >= gi else 0
res += pc * 3 if ci > pc else ci * 3
ci, pc = ci - pc if ci >= pc else 0, pc - ci if pc >= ci else 0
res += gc * 3 if pi > gc else pi * 3
pi, gc = pi - gc if pi >= gc else 0, gc - pi if gc >= pi else 0

# same count
res += min(gi, gc)
res += min(pi, pc)
res += min(ci, cc)

print(res)
