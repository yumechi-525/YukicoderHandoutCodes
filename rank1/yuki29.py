N = int(input())
table =[0 for _ in range(10)]
for _ in range(N):
    a, b, c = map(lambda x: int(x) - 1, input().split())
    table[a] += 1
    table[b] += 1
    table[c] += 1

res = 0
for i in range(10):
    while table[i] > 1:
        table[i] -= 2
        res += 1

print(res + sum(table) // 4)
