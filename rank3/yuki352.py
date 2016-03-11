from itertools import combinations

def solve():
    n = int(input())
    fact = [1]*21
    for i in range(1, 21):
        fact[i] *= (i+1) * fact[i-1]
    res = 1.0
    for i in range(2, n+1):
        tres = 2 * (1 / i)
        for elem in combinations([j for j in range(1, i)], 2):
            tres += elem[0] * elem[1] * 2 * (fact[i-3] / fact[i-2]) * (1 / i)
        res += tres
    print(res)

if __name__=="__main__":
    solve()