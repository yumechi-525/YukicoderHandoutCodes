def solve():
    w, h = map(int, input().split())
    px, py, qx, qy = -1, -1, -1, -1
    for y in range(w):
        line = input()
        while "*" in line:
            idx = line.find("*")
            if px == -1:
                px, py = idx, y
            else:
                if len(line) == h:
                    qx, qy = idx, y
                else:
                    qx, qy = idx + px + 1, y
            line = line[idx+1:]
    tx, ty = -1, -1
    patternlist = [[px-1, px+1, qx-1, qx+1], [py-1, py+1, qy-1, qy+1]]
    for j in range(4):
        for k in range(4):
            x, y = patternlist[0][j], patternlist[1][k]
            if (0 <= x < h and 0 <= y < w) \
                and (not(x == px and y == py)) and (not(x == qx and y == qy)) \
                and not(px - x == py - y and qx - x == qy - y):
                tx, ty = x, y
                break
        if tx != -1:
            break

    points = [[px, qx, tx], [py, qy, ty]]
    ans = [list("-" * h) for _ in range(w)]
    for i in range(3):
        ans[points[1][i]][points[0][i]] = "*"
    print("\n".join(["".join(line) for line in ans]))

if __name__=="__main__":
    solve()