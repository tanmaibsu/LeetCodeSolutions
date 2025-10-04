import re
def myAtoi(s: str) -> int:
    if s == "" or s == "+" or s == "-" or s == " ":
        return 0
    sanitized_str = ""

    for i, st in enumerate(s):
        if len(sanitized_str) == 0 and st == " ":
            continue
        if len(sanitized_str) == 0 and (st == "+" or st == "-"):
            sanitized_str = sanitized_str + st
            continue
        if len(sanitized_str) == 0 and not st.isdecimal():
            return 0
        if len(sanitized_str) > 0 and not st.isdecimal():
            try: 
                int_str = int(sanitized_str)
            except (ValueError, TypeError):
                return 0    
            if int_str < -(2**31):
                return -(2**31)
            if int_str > (2**31) - 1:
                return (2**31) - 1
            else:
                return int_str
        
        sanitized_str = sanitized_str + st
        try: 
            int_str = int(sanitized_str)
        except (ValueError, TypeError):
            return 0 
    if int_str < -(2**31):
        return -(2**31)
    if int_str > (2**31) - 1:
        return (2**31) - 1
    else:
        return int_str


print(myAtoi("  -0012a42"))

