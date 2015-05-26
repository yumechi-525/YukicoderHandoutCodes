so = [2,3,5,7,11,13]
go = [4,6,8,9,10,12]
table = [0 for _ in range(201)]
for s in so:
    for g in go:
        table[s*g] += 1
print(table[int(input())] / 36)