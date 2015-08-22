from math import factorial

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
    res *= factorial(length) // (factorial(length - i) * factorial(i))
    length -= i
print((res-1) % 573)
