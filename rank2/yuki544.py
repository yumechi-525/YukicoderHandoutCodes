def solve():
    lis = list(input())
    ans = ["0"]*len(lis)
    ans2 = ["0"]*len(lis)
    for idx, elem in enumerate(lis):
        if elem == "7":
            ans[idx] = "6"
            ans2[idx] = "1"
        else:
            ans[idx] = elem
    print("".join(ans), int("".join(ans2)))


if __name__=="__main__":
    solve()
