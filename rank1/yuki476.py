a,b=map(int,input().split())
print("YES" if b == sum([int(i) for i in input().split()])/a else "NO")
