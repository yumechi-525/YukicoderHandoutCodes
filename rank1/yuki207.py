A, B = map(int, input().split())
for i in range(A, B + 1):
    if i % 3 == 0 or str(i).find("3") != -1:
        print(i)