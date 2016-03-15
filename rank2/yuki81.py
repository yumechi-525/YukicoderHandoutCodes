from decimal import *

def solve():
    n = int(input())
    getcontext().prec = 25
    num = Decimal("0.0")
    for _ in range(n):
        num += Decimal(input())
    res = str(num)
    dot_idx = res.find(".")
    if(len(res[dot_idx+1:]) <= 10):
        res += "0" * (11 - (len(res) - dot_idx))
    print(res)

if __name__=="__main__":
    solve()