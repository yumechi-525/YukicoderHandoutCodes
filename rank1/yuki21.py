N = int(input())
K = int(input())
nlist = []
for _ in range(N):
    nlist.append(int(input()))
print(int(max(nlist) - min(nlist)))
