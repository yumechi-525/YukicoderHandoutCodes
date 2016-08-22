def solve():
    s1, t = input().split()
    t = int(t)
    t = t if t > 0 else (12 - -t)
    clockchar = ["XII", "I","II","III","IIII","V","VI","VII","VIII","IX","X","XI"]
    print(clockchar[(clockchar.index(s1) + int(t)) % 12])

if __name__=="__main__":
    solve()