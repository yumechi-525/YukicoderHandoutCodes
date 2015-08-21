N = int(input())
li = []
mw = 0
for i in range(N):
    a, b = map(int, input().split())
    w = a + b * 4
    mw = max(mw, w)
    li.append(w)

# imcalculate check
eli = [i for i in li if i % 2 == 0]
if len(eli) != N and len(eli) != 0:
    print(-1)
    exit(0)

res = 0
for elem in li:
    res += (mw) - elem
print(res)
