l1, l2, l3 = map(int, input().split())
llist = [[l1, l2], [l2, l3], [l3, l1]]
r, b, y = map(int, input().split())
res = 10 ** 9 + 7
for i in range(3):
    rt = sum(llist[i]) * 2 * r
    for j in range(2):
        bt = sum(llist[(i+1+j) % 3]) * 2 * b
        yt = sum(llist[(i+2-j) % 3]) * 2 * y
        tres = rt + bt + yt
        res = min(tres, res)
print(res)
