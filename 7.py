def reverse(x: int) -> int:
        neg = False
        if (x == 0):
            return 0
        if(x < 0):
            neg = True
            x = -(x)
        res = 0
        while (x != 0):
            print("I am here")
            rem = x % 10
            res = res*10 + rem
            print(res)
            x = x // 10
        if neg:
            res = -res
            if res <= -(2**31):
                return 0
        else:
            if res >= 2**32 - 1:
                return 0
        return res

print(reverse(123))