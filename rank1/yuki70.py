N = int(input())
res = 0
for i in range(N):
    first, second = input().split(" ")
    fh, fm = map(int, first.split(":"))
    sh, sm = map(int, second.split(":"))
    if fh > sh:
        sh += 24
    if fm > sm:
        sh -= 1
        sm += 60
    res += (sh - fh) * 60 + (sm - fm)
print(res)
