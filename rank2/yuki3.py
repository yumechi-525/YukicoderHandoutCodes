N = int(input())
numberlist = []
for i in range(1, N+1):
    num = str(bin(i)).count("1")
    numberlist.append(num)
visited = set([1])
search = [[1, 1]]

while len(search) > 0:
    cur, turn = search.pop(0)
    if cur == N:
        print(turn)
        exit(0)
    mv = numberlist[cur-1]
    if cur - mv > 1 and (cur - mv) not in visited:
        search.append([cur - mv, turn + 1])
        visited.update(set([cur - mv]))
    if cur + mv <= N and (cur + mv) not in visited:
        search.append([cur + mv, turn + 1])
        visited.update(set([cur - mv]))

print(-1)
