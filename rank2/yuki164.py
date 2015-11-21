res = -1
for _ in range(int(input())):
    inp = input()
    while inp[0] == "0" and len(inp) > 1:
        inp = inp[1:]
    decimal = 2
    for c in inp:
        tdec = 0
        if c.isdigit():
            tdec = int(c) + 1
        else:
            tdec = ord(c) - ord('A') + 11
        decimal = max(tdec, decimal)
    res = min(res, int(inp, decimal)) if res != -1 else int(inp, decimal)
print(res)