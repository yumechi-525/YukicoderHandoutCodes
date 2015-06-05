i = [int(input()) for _ in range(3)]
i[1] = i[0] // i[1] + (0 if i[0] % i[1] == 0 else 1)
i[2] = i[0] // i[2] + (0 if i[0] % i[2] == 0 else 1)
print("YES" if i[1] * 2 - i[2] * 3 >= 0 else "NO")