import itertools

S = input()
dic = dict()
for c in S:
    if c not in dic:
        dic.update({c:1})
    else:
        dic[c] += 1

length = len(S)
res = 1
vs = [i for i in dic.values()]
vs.sort()
vs = vs[::-1]

for i in vs:
    res *= len(list(itertools.combinations(range(length), i)))
    length -= i
print(res-1)
