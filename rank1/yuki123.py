N, M = map(int, input().split())
ali = list(map(lambda x: int(x) - 1, input().split()))
vli = [i+1 for i in range(N)]
for a in ali:
    vli = [vli[a]] + vli[:a] + vli[a+1:]
print(vli[0])
