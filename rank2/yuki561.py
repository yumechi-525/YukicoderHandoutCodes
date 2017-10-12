def solve():
    n, d = map(int, input().split())
    t, k = map(int, input().split())
    k -= d
    for _ in range(n-1):
        lt, lk = t, k
        nt, nk = map(int, input().split())
        t = max(lt + nt, lk - d + nt)
        k = max(lk + nk, lt - d + nk)
    print(max(t, k))

if __name__=="__main__":
    solve()
