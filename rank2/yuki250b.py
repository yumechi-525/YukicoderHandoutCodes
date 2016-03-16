from math import factorial
 
def solve():
    fact = [factorial(i) for i in range(3001)]

    for i in range(int(input())):
        d, x, t = map(int, input().split())
        n = (d + x - 1)
        r = x if (n//2 > x) else (n - x)
        ans = fact[n] // (fact[n - r] * fact[r])
        print("AC" if ans <= t else "ZETUBOU")

if __name__=="__main__":
    solve()