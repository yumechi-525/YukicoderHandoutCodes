from math import sqrt
import collections

def primeFactorization(n):
    ret = []
    for i in range(2, int(sqrt(n) + 2)):
        while n % i == 0:
            n //= i
            ret.append(i)
    if n > 1:
        ret.append(n)
    return ret

x = int(input())
counter = collections.Counter(primeFactorization(x))
res = 1
for k, v in counter.items():
    if v % 2 == 1:
        res *= k
print(res)
