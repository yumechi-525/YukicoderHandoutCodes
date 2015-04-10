N = int(input())
M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    if A == N:
        N = B
    elif B == N:
        N = A
print(N)
