mark2number = {"A":1, "T":10, "J":11, "Q":12, "K":13}
number2mark = {1:"A", 10:"T", 11:"J", 12:"Q", 13:"K"}
cardmark2number = {"D":0, "C":1, "H":2, "S":3}
number2cardmark = {0:"D", 1:"C", 2:"H", 3:"S"}
cardlist = [[] for _ in range(4)]

n = int(input())
for s in input().split():
    s0, s1 = s[0], s[1]
    cardlist[cardmark2number[s0]].append(s1)

for i in range(4):
    for j in range(len(cardlist[i])):
        if cardlist[i][j] in mark2number:
            cardlist[i][j] = mark2number[cardlist[i][j]]
        else:
            cardlist[i][j] = int(cardlist[i][j])

for i in range(4):
    cardlist[i].sort()

for i in range(4):
    for j in range(len(cardlist[i])):
        if cardlist[i][j] in number2mark:
            cardlist[i][j] = number2mark[cardlist[i][j]]
        else:
            cardlist[i][j] = str(cardlist[i][j])

res = ""
for i in range(4):
    for j in range(len(cardlist[i])):
        cardlist[i][j] = number2cardmark[i] + cardlist[i][j]
    res += " ".join(cardlist[i])
    if i != 3 and len(cardlist[i]) > 0:
        res += " "

print(res)
