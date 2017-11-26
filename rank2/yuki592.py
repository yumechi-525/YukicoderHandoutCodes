N = int(input())
S = input()
leftcounter = rightcounter = 0
llist, rlist, tlist = [], [], []
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
            tlist.append([l, r])

ans = [0]*N
for e in tlist:
    ans[e[0]-1] = str(e[1])
    ans[e[1]-1] = str(e[0])
print("\n".join(ans))
