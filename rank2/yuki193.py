__author__ = 'student'
S = input()
maxnum = -9999999999999999999999999
length = len(S)
checknum = lambda x, line: not (line[x] == "+" or line[x] == "-")
for i in range(length):
    line = S[i:length] + S[0:i]
    tline = line

    if not checknum(0, line) or not checknum(len(line) - 1, line):
        continue

    j = 0
    while tline[j] == "0":
        j += 1
    if not checknum(j, tline):
        tline = tline[j - 1:len(tline)]

    j = 1
    while j < len(tline):
        if not checknum(j - 1, tline) and tline[j] == "0":
            if j == len(tline) - 1:
                break
            else:
                if checknum(j + 1, tline):
                    tline = tline[0:j] + tline[j+1:len(tline)]
        else:
            j += 1

    for i in range(len(tline) - 1):
        if not checknum(i, tline) and not checknum(i + 1, tline):
            line = ""
            break
    else:
        line = tline

    try:
        maxnum = max(maxnum, eval(line))
    except:
        pass
print(maxnum)