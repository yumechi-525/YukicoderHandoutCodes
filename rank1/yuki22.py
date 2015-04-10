N, K = map(int, input().split())
S = input()
leftcounter = rightcounter = 0
llist, rlist, list = [], [], []
for i in range(N):
    if S[i] == "(":
        leftcounter += 1
        llist.append(i + 1)
    if S[i] == ")":
        rightcounter += 1
        rlist.append(i + 1)
        if leftcounter >= rightcounter:
            l = llist.pop()
            r = rlist.pop()
            list.append([l, r])

for i in range(2):
    for j in range(len(list)):
        if list[j][i] == K:
            print(list[j][1] if i == 0 else list[j][0])
            break
