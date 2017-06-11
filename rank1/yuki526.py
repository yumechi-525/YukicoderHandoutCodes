def solve():
    n, m = map(int, input().split())
    a1, a2 = 0, 1
    for i in range(2, n+1):
        a1, a2 = (a1 + a2) % m, a1 % m
    print(a1)


if __name__=="__main__":
    solve()
