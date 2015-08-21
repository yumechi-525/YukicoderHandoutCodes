import math

W, D = int(input()), int(input())
for i in range(D-1):
    cday = D - i
    W -= math.floor(W / (cday ** 2))
print(W)
