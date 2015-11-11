W, H, N = [int(input()) for _ in range(3)]
res = 0
visitW, visitH = set([]), set([])
for i in range(N):
    s, k = map(int, input().split())
    if s in visitW and k in visitH:
        res -= 1
    elif k in visitH:
        res += H - len(visitH) - 1
        visitW.update(set([s]))
    elif s in visitW:
        res += W - len(visitW) - 1
        visitH.update(set([k]))
    else:
        res += W + H - len(visitW) - len(visitH) - 2
        visitW.update(set([s]))
        visitH.update(set([k]))
    # print(res, visitW, visitH)
print(res)
