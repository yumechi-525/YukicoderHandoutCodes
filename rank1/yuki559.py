def solve():
    s = input()
    cntA = s.count("A")

    ans = 0
    while s[:cntA].count("A") != cntA:
        bl = s.rfind("B")
        ar = s.rfind("A")
        ans += len(s) - bl - 1
        s = s[:bl] + s[bl+1:ar+1] 
    print(ans) 

if __name__=="__main__":
    solve()
