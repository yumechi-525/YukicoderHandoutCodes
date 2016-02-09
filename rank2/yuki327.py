# please use positive value
def convertDecimal(
            num, \
            decimal, \
            characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
            lowercharacter=False \
    ):
    
    # decimal only can use 2 to 36
    if num < 0 and not 2 <= decimal <= 36:
        return None

    ret = ""
    while num > 0:
        ret = characters[num % decimal] + ret
        num //= decimal
    return ret

def solve(num):
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = words[num % 26]
    while num >= 26:
        ret = words[(num//26-1) % 26] + ret
        num //= 26
        num -= 1
    return ret

if __name__=="__main__":
    print(solve(int(input())))
