def solve():
    for _ in range(int(input())):
        i = int(input())
        res = ""
        while i > 0:
            if i % 2 == 0:
                i -= 1
                res += "R"
            else:
                res += "L"
            i >>= 1
        print(res[::-1])


if __name__=="__main__":
    solve()
