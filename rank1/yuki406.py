def solve():
    n = int(input())
    xl = sorted([int(i) for i in input().split()])

    # condition 1
    if len(set(xl)) != n:
        print("NO")
        return

    #condition 2
    print("YES" if len(set([xl[i] - xl[i+1] for i in range(n-1)])) == 1 else "NO")

if __name__=="__main__":
    solve()