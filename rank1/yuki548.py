def solve():
    ng = "Impossible"
    d = {chr(97+i):1 for i in range(13)}
    for c in input():
        if c not in d.keys():
            print(ng)
            return
        d[c] -= 1
    if len([i for i in d.values() if i == 0]) == 13:
        print("\n".join([chr(97+i) for i in range(13)]))
    else:
        ans = [i[0] for i in d.items() if i[1] > 0]
        print(ng if len(ans) >= 2 else ans[0])

if __name__=="__main__":
    solve()
