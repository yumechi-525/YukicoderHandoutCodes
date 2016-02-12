def solve(num):
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = words[num % 26]
    while num >= 26:
        ret = words[(num//26-1) % 26] + ret
        num //= 26
        num -= 1
    return ret

if __name__=="__main__":
    print(solve(int(input())))
