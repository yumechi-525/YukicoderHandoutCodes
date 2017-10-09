N = int(input())
arr = list(map(int, input().split()))
dic = {}
for a in arr:
    if a not in dic:
        dic.update({a:1})
    else:
        dic[a] += 1
maxkey = -1
maxval = -111
for k, v in sorted(dic.items()):
    if v >= maxval:
        maxval = v
        maxkey = max(maxkey, k)
print(maxkey)
