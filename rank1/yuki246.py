i, y = map(int, input().split())
r = i - y
if r == 0:
    print("Drew")
elif r == -1 or r == 2:
    print("Won")
else:
    print("Lost")