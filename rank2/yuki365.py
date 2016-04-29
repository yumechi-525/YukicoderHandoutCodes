def solve():
    n = int(input())
    al = [int(i) for i in input().split()]

    res = n
    for i in al[::-1]:
        if res == i:
            res -= 1
    print(res)

if __name__=='__main__':
    solve()