n = input()
d = {}
for c in input().split():
    i = int(c)
    if i not in d:
        d.update({i:1})
    else:
        d[i] += 1
print(sum([1 for i in d.values() if i == 1]))
