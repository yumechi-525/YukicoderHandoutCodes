S = input()
res = ""
N = len(S)
for i in range(1, N + 1):
    asciic = ord(S[i - 1]) - i
    while ord("A") > asciic:
        asciic += 26
    res += chr(asciic)
print(res)