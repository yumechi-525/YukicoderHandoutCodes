def roman2arabic(roman: str) -> int:
    special_case = { "IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900 }
    normal_case = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
    arabic = 0
    for s in special_case.keys():
        if s in roman:
            arabic += special_case[s]
            roman = roman.replace(s, "")
    for n in normal_case.keys():
        if n in roman:
            arabic += roman.count(n) * normal_case[n]
    return arabic

def arabic2roman(arabic: int) -> str:
    if arabic > 3999:
        return "ERROR"
    roman = ""
    roman_numerics = { 1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L", 40 : "XL", 10 : "X", 9 : "IX", 5 : "V", 4 : "IV", 1 : "I" }
    while arabic > 0:
        for n in roman_numerics.keys():
            if arabic >= n:
                roman += roman_numerics[n]
                arabic -= n
                break
    return roman 

def solve():
    input()
    print(arabic2roman(sum([roman2arabic(i) for i in input().split()])))

if __name__=="__main__":
    solve()
