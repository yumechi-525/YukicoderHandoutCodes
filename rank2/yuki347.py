from math import log

def solve():
    n, b = int(input()), int(input())
    data = [float(f) for f in input().split()]
    res1, res2 = 0.0, 0.0
    
    for f in data:
        if f == 0.0:
            continue
        f1 = f - 1
        res1 += f * (b ** f1)
    print(res1)
    
    for f in data:
        f1 = f + 1
        if f == -1.0:
            res2 += log(b)
        else:
            res2 += (1 / f1) * (b ** (f + 1))
    print(res2)

if __name__=="__main__":
    solve()