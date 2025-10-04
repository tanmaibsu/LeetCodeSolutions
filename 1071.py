def gcdOfStrings(str1: str, str2: str) -> str:
        
        gcd1 = ""
        gcd2 = ""
        n = len(str1)
        n1 = len(str2)

        i = 0
        while i < n1:
            if str2[i] not in gcd1:
                gcd1 = gcd1 + str2[i]
            i += 1
        
        i = 0
        while i < n:
            if str1[i] not in gcd2:
                gcd2 = gcd2 + str1[i]
            i += 1

        if gcd1 == gcd2:
            return gcd1
        else:
            return ""

print(gcdOfStrings("ABCABC", "ABC"))