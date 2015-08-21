s = input()
res = "1"
for c in s:
    if c == "L":
        res += "0"
    if c == "R":
        res += "1"
print(int(res, 2))
