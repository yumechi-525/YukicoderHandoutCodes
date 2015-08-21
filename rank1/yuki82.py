w, h, c = input().split()
w, h = int(w), int(h)
rc = "B" if c == "W" else "W"
for i in range(h):
    line = ""
    for j in range(w):
        if i % 2 == 0:
            if j % 2 == 0:
                line += c
            else:
                line += rc
        else:
            if j % 2 == 0:
                line += rc
            else:
                line += c
    print(line)
