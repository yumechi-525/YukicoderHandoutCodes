def solve():
    px, py = map(int, input().split())
    qx, qy = map(int, input().split())

    print((abs(px - qx) + abs(py - qy)) / 2)


if __name__=="__main__":
    solve()