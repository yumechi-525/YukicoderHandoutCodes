numstrs = []
pluscount = 0
minuscount = 0

N = int(input())
for c in input().split():
    if c == "+":
        pluscount += 1
    elif c == "-":
        minuscount += 1
    else:
        numstrs.append(c)

numstrs.sort(reverse=True)
bignum = ""
bigres = 0
numcount = len(numstrs)
for i in range(numcount - pluscount - minuscount):
    bignum += numstrs[i]
bigres += int(bignum)
for i in range(numcount - pluscount - minuscount, numcount - minuscount):
    bigres += int(numstrs[i])
for i in range(numcount - minuscount, numcount):
    bigres -= int(numstrs[i])

minres = 0
if minuscount >= 1:
    for i in range(numcount - pluscount - 1, numcount):
        minres += int(numstrs[i])
    for i in range(len(bignum), numcount - pluscount - 1):
        minres -= int(numstrs[i])
    minres -= int(bignum)
else:
    li = ["" for i in range(pluscount + 1)]
    for i in range(numcount - 1, -1, -1):
        li[i % (pluscount + 1)] += numstrs[i]
    minres = sum([int(i) for i in li])

print(bigres, minres)