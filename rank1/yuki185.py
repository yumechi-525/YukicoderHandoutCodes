N = int(input())
a, b = map(int, input().split())
res = b - a
if res < 1:
    print(-1)
    exit(0)
for _ in range(N-1):
    a, b = map(int, input().split())
    if res != b - a:
        print(-1)
        exit(0)
print(res)