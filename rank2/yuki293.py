i, j = map(int, input().split())
if len(str(i)) != len(str(j)):
    print(i if i > j else j)
    exit(0)
for k in range(len(str(i)),0,-1):
    t = 10 ** (k - 1)
    ik, jk = i // t % 10, j // t % 10
    if ik != jk:
        if (ik == 4 and jk == 7) or (ik == 7 and jk == 4):
            print(i if ik == 4 else j)
        else:
            print(i if ik > jk else j)
        exit(0)