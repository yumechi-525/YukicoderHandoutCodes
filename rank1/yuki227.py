dic = dict([])
for i in map(int, input().split()):
    if i in dic:
        dic[i] += 1
    else:
        dic.update({i:1})

twop, threec = 0, 0
for v in dic.values():
    if v == 2:
        twop += 1
    if v == 3:
        threec += 1

ans = ["NO HAND", "ONE PAIR", "TWO PAIR", "THREE CARD", "FULL HOUSE"]
print(ans[twop + threec * 3])