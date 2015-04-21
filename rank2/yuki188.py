month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = 0
for i in range(1, 13):
    for j in range(1, month[i-1] + 1):
        if i == j // 10 + j % 10:
            res += 1
print(res)