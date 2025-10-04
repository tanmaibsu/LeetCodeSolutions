def divide(dividend: int, divisor: int) -> int:

    if dividend == 0:
        return 0

    sign = 1

    UPPER = ((2**31) - 1)
    LOWER = -(2**31)

    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1

    dividend = abs(dividend)
    divisor = abs(divisor)

    count = 0

    if dividend == divisor:
        return sign

    if divisor == 1:
        count = dividend
    else:
        while(dividend >= divisor):
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                print("multiple->", multiple)

            print("temp->", temp)
            dividend -= temp
            print("dividend->", dividend)
            count += multiple
            print("multiple->", multiple)
    
    count = count*sign

    if count > UPPER:
        return UPPER
    elif count < LOWER:
        return LOWER
        
    return count


print(divide(-231, 3))