S = input()
maxnum = -9999999999999999999999999
length = len(S)
ckecknum = lambda x: not (x == "+" or x == "-")
for i in range(length):
    line = S[i:length] + S[0:i]

    # first and end check
    first = line[0]
    end = line[length - 1]
    if not ckecknum(first) or not ckecknum(end):
        line = ""
        continue
    
    try:
        maxnum = max(maxnum, eval(line))
    except:
        pass
print(maxnum)