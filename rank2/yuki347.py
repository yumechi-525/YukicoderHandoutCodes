from math import log

def solve():
    n, b = int(input()), int(input())
    data = input().split()
    res1, res2 = 0.0, 0.0
    
    for d in data:
        if d == "0.0":
            continue
        f = float(d)
        f1 = f - 1
        res1 += f * (b ** f1)
    print(res1)
    
    for d in data:
        if d == "-1.0":
            res2 += log(b)
        else:
            f = float(d)
            f1 = f + 1
            res2 += (1 / f1) * (b ** (f + 1))
    print(res2)

if __name__=="__main__":
    solve()