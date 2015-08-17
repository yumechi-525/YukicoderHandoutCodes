res = 0
for i in range(int(input())):
    c, d = map(int, input().split())
    res += (c + 1) // 2 * d
print(res % (10 ** 9 + 7))