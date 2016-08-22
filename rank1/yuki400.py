def solve():
    print("".join(map(lambda x: ">" if x == "<" else "<", input()[::-1])))

if __name__=="__main__":
    solve()