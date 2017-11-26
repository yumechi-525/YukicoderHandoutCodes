def solve():
    n = input()

    i3, i5, t = 0, 0, 0
    for i, v in enumerate(n[::-1]):
        tv = int(v)
        i3 += tv
        if i == 0:
            t = tv * 1
        else: 
            t = tv * [4, 6][(i + 1) % 2]
        t %= 10
        i5 += t
        i3, i5 = i3 % 3, i5 % 5
    print(((i3 == 0 and "Fizz" or "") + (i5 == 0 and "Buzz" or "")) or n)

if __name__=="__main__":
    solve()
