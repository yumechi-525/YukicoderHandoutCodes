N = int(input())
progli = list(map(int, input().split()))
scoreli = list(map(int, input().split()))
scoremap = {0:0}
for i in range(N):
    if scoreli[i] in scoremap:
        scoremap[scoreli[i]] += progli[i]
    else:
        scoremap.update({scoreli[i]:progli[i]})

maxid = 0
maxval = scoremap[0]
for k, v in scoremap.items():
    if maxval < v:
        maxval = v
        maxid = k

print("YES" if maxid == 0 else "NO")