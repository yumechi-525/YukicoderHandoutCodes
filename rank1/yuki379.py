from decimal import *

def solve():
    getcontext().prec = 50
    n, g, v = [int(i) for i in input().split()]
    print(Decimal((n - n % 5) // 5) * Decimal(g) / Decimal(v))

if __name__=="__main__":
    solve()