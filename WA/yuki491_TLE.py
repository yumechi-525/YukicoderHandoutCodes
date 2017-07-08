def solve():
    n = int(input())
    ans = 0
    num = 10 ** 9 + 1

    cnt = 1
    while num * cnt <= n:
        comp_num_str = str(num * cnt)
        lotation_flag = True
        for k in range(len(comp_num_str) // 2):
            if comp_num_str[k] != comp_num_str[-k-1]:
                lotation_flag = False
                break
        if lotation_flag:
            print(cnt, num * cnt)
        cnt += 1

        """
    for i in range(len(str(n // (10 ** 9)))):
        for j in range(1, 10):
            comp_num_str = str(num * int(str(j) * (i + 1)))
            print(comp_num_str, int(str(j) * (i + 1)))
            lotation_flag = True
            for k in range(len(comp_num_str) // 2):
                if comp_num_str[k] != comp_num_str[-k-1]:
                    lotation_flag = False
                    break
            if not lotation_flag:
                continue
            if int(comp_num_str) <= n:
                ans += 1
            else:
                break
        """

    print(ans)

if __name__=="__main__":
    solve()
