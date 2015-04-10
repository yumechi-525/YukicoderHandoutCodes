hundred = int(input())
quarter = int(input())
one = int(input())
kouka = 0
total =  (hundred * 100 + quarter * 25 + one * 1) % 1000
kouka += total // 100
total %= 100
kouka += total // 25 + total % 25
print(kouka)
