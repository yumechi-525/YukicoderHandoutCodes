n = int(input())
li = list(map(int, input().split()))
el = len([i for i in li if i % 2 == 0])
print(abs(n - 2 * el))
