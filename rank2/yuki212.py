P, C = map(int, input().split())
exps = (sum([2,3,5,7,11,13]) / 6)** P
expg = (sum([4,6,8,9,10,12]) / 6) ** C
print(exps * expg)