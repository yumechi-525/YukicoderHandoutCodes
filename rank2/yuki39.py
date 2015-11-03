s = input()
res = int(s)
for i in range(len(s)):
    for j in range(i+1, len(s)):
        t = int(s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:])
        res = max(res, t)
print(res)
