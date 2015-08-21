import math

x, y = map(int, input().split())
length = math.sqrt(x ** 2 + y ** 2) * 2
checker = math.ceil(length)
print(checker if length != checker else checker + 1)
