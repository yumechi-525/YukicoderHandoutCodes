w, h, c = input().split()
w, h = int(w), int(h)
rc = "B" if c == "W" else "W"
for i in range(h):
    line = ""
    for j in range(w):
        line += c if j % 2 == 0 else rc
    c, rc = rc, c
    print(line)
