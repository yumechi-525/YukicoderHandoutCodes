from operator import add

def solve():
    a, b = map(int, input().split())
    print(add(a, b))


if __name__=="__main__":
    solve()