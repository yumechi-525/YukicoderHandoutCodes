def solve():
    n = int(input())
    al = [int(i) for i in input().split()]
    for i in range(1, 2 * n - 3):
        for j in range(n - 1):
            p, q = j, i - j
            if 0 <= p < q <= n - 1 and al[p] > al[q]:
                al[p], al[q] = al[q], al[p]
    print(*al)

if __name__=="__main__":
    solve()
