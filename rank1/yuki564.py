def solve():
    h, n = map(int, input().split())
    hl = [int(input()) for _ in range(n-1)]
    hl.append(h)
    hl.sort(reverse=True)
    ans = hl.index(h)
    ans_ext = ["st", "nd", "rd"]
    ans_ext.extend(["th" for _ in range(7)])
    print("{0}{1}".format(ans+1, ans_ext[ans%10]))


if __name__=="__main__":
    solve()
