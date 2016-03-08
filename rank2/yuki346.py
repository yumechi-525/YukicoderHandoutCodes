def solve(s):
    # s = input()[::-1]
    s = s[::-1]
    wc = 0

    res = 0
    for c in s:
        if c == "c":
            if wc >= 2:
                res += (wc * (wc-1)) // 2
            continue
        if c == "w":
            wc += 1
    return res

def test():
    mxnum = 0
    idx = 0
    for i in range(0, 100001):
        r = solve("c" * i + "w" * (100000 - i))
        print(i, r)
        if r > mxnum:
            mxnum = r
            idx = i
    print("\n" * 3)
    print("***最大ケース***")
    print("idx = %d, mxnum = %d" % (idx, mxnum))

if __name__=="__main__":
    solve(input())
    