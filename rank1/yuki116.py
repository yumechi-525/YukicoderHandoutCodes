n = int(input())
ali = list(map(int, input().split()))
res = 0
for i in range(n-2):
    cli = list(set(ali[i:i+3]))
    cli.sort()
    if len(cli) == 3 and (ali[i] == cli[1] or ali[i+2] == cli[1]):
        res += 1
print(res)
