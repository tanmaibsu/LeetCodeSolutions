def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = len(s) - 1
        # print(l)

        i = 0
        while i <= l/2:
            temp = s[l-i]
            s[l-i] = s[i]
            s[i] = temp
            print(s)
            i += 1

        return s  
        
        

print(reverseString(["H","a","n","n","a","h"]))