res = ""
for c in list(input()):
    res += c.upper() if c.islower() else c.lower()
print(res)