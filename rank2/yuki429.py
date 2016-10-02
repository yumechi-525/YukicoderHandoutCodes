def solve():
    n, k, x = map(int, input().split())
    start = [i for i in range(n)]
    executelist = []
    for i in range(k):
        li = input().split()
        a, b = 0, 0
        if(i != x-1):
            a, b = map(lambda inp: int(inp)-1, li)
        else:
            a, b = "?", "?"
        executelist.append([a, b])
    end = [int(i) - 1 for i in input().split()]

    for i in range(x-1):
        f, s = executelist[i][0], executelist[i][1]
        start[f], start[s] = start[s], start[f]
    for i in range(k-1, x-1, -1):
        f, s = executelist[i][0], executelist[i][1]
        end[f], end[s] = end[s], end[f]
    ans = []
    for i in range(n):
        if start[i] != end[i]:
            ans.append(i+1)
    print(*ans)

if __name__=="__main__":
    solve()