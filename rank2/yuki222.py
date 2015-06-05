s = list(input())
a, b = 0, 0

op = ""

minus = False
if s[0] == "-":
    minus = True
    s.pop(0)
if s[0] == "+":
    s.pop(0)
idx = 0
while s[idx].isdigit():
    idx += 1
num = int("".join(s[:idx]))
s = s[idx:]
a = num if not minus else -num

op = s[0]
if op == "+":
    op = "-"
else:
    op = "+"
s.pop(0)

minus = False
if s[0] == "-":
    minus = True
    s.pop(0)
if s[0] == "+":
    s.pop(0)
idx = 0
while idx < len(s) and s[idx].isdigit():
    idx += 1
num = int("".join(s[:idx]))
s = s[idx:]
b = num if not minus else -num

print(a-b if op == "-" else a+b)