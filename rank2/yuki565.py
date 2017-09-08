def solve():
    r, k = map(int, input().split())
    h, w = map(int, input().split())
    cl = [[i for i in list(input())] for _ in range(h)]
    for _ in range(r//90):
        cl = [[cl[j][i] for j in range(h)][::-1] for i in range(w)]
        w, h = h, w
    print("\n".join(["".join(a) for a in [[cl[i//k][j//k] for j in range(w * k)] for i in range(h * k)]]))

if __name__=="__main__":
    solve()
