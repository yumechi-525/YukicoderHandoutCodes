N = int(input())
ali = list(map(int, input().split()))
mx = max(ali)
mi = min(ali)
if(mx != mi):
    print(ali.count(mx), ali.count(mi))
else:
    if mx // 4 == N - 1:
        print(0, N)
    else:
        print(N, 0)
