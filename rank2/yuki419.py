from decimal import *

def solve():
    getcontext().prec = 25
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    if a != b:
        print(Decimal(Decimal(a) ** Decimal(2) - Decimal(b) ** Decimal(2)) ** Decimal(0.5))
    else:
        print(Decimal(Decimal(a) ** Decimal(2) + Decimal(b) ** Decimal(2)) ** Decimal(0.5))


if __name__=="__main__":
    solve()
