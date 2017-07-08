def solve():
    n, d = map(int, input().split())
    if d == 0:
        print("C" * n)
    elif n >= d:
        print("A" * d + "C" * (n - d))
    else:
        print("A" * (n - (d - n)) + "B" * (d - n))

if __name__=="__main__":
    solve()