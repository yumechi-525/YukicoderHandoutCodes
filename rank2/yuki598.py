import math

def solve():
    n, x, a, b = [int(input()) for _ in [0]*4]
    bits_list = [2 ** i for i in range(33)]
    overflag = bits_list[n - 1]
    ta = math.ceil(x / a)
    tb = math.ceil((overflag - x) / b)
    print(min(ta, tb))

if __name__=="__main__":
    solve()
