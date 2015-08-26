N, M = int(input()) % 10, int(input())
print(1 if M == 0 else (N ** (M % 4 + 4)) % 10)
