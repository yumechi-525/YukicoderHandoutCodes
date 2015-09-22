d = {"t":0, "r":0, "e":0}
for c in list(input()):
    if c in d:
        d[c] += 1
print(min(d["t"], d["r"], d["e"]//2))
