def largestGoodInteger(num: str) -> str:
    sub_str = ""
    sub_strs = []
    l = 1
    for i, elm in enumerate(num):
        if l == 3:
            sub_strs.append(sub_str*3)
        if i < len(num) - 1 and int(elm) == int(num[i+1]):
            sub_str = elm
            l += 1
        else:
            l = 1
            sub_str = elm
    if len(sub_strs) == 1:
        return sub_strs[0]
    elif len(sub_strs) > 1:
        max_i = -100
        sub_strs_i = []
        for i, elm in enumerate(sub_strs):
           sub_strs_i.append(int(elm))
        if max(sub_strs_i) == 0:
            return str(0)*3
        else:
            return str(max(sub_strs_i))
    return ""

print(largestGoodInteger("3200014888"))