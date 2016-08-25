import array

def solve():
    n, l = map(int, input().split())
    ans = 0
    nummax = l // (n - 1) + 1
    if nummax < 2:
        print(0)
        return
    primes = array.array("B", (True for i in range(nummax)))
    primes[0], primes[1] = False, False
    taprime = []
    for i in range(2, nummax):
        if primes[i]:
            for j in range(2 * i, nummax, i):
                primes[j] = False
            taprime.append(i)

    for i in taprime:
        t = (l + 1) - (n - 1) * i
        if t <= 0:
            break
        ans += t
    print(ans)

if __name__=="__main__":
    solve()