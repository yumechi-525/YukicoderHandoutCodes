def solve():
    n = int(input())
    arr, nc = [], n
    while nc > 0:
        arr.append(nc)
        nc //= 2
    arr.append(0)
    standardscore = sum(arr)
    print(arr[0] + arr[1] * 2 + (arr[0] % 2 == 1 if 1 else 0) - standardscore)

if __name__=="__main__":
    solve()