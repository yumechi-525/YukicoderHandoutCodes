p = int(input())
for _ in range(p):
    N, K = map(int, input().split())
    if N - 1 <= K:
        print("Win")
        continue
    print("Win" if N % (K + 1) != 1 else "Lose")
