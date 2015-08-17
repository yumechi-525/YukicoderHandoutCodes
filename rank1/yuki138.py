f = lambda : list(map(int, input().split(".")))
print("YES" if  f() >= f() else "NO")