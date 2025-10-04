def intToRoman(num: int) -> str:
    roman_to_integer = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    romans = ""

    while(True):
        print(num)
        if num < 1:
            return romans
            break
        if num < 5:
            if num == 4:
                romans += "IV"
                num -= 4
                continue
            if num < 4:
                num += "I"
                num -= 4
                continue
        if num < 10 
        if num == 9:
            romans += "IX"
            num -= 9
            continue
        if num > 500 and num < 1000:

            romans += "D"
            num -= 500
            continue
        if num > 1000 :
            romans += "M"
            num -= 1000
            continue
        break
            

print(intToRoman(3749))