N = int(input())
res = ""
if N % 2 == 1:
    res += "7"
    N -= 3
for i in range(N // 2):
    res += "1"
print(res)
