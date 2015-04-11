N = int(input())
SECOND = 1000
cantype = 12
typed = miss = 0
for _ in range(N):
    A, B = input().split()
    A = int(A)
    t = len(B) - int(A / 1000 * 12)
    if t <= 0:
        typed += len(B)
    else:
        typed += len(B) - t
        miss += t
print(typed, miss)
