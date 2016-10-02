from collections import defaultdict

def solve():
    s = input()
    slist = defaultdict(lambda: 0)
    slen = len(s)
    for i in range(1, 11):
        if i <= slen:
            for j in range(slen-i+1):
                slist[s[j:j+i]] += 1
    ans = 0
    for i in range(int(input())):
        ans += slist[input()]
    print(ans)

if __name__=="__main__":
    solve()