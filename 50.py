def myPow(x: float, n: int) -> float:
        
    if n == 0:
        return 1

    res = 1
    x_sign = 1
    n_pos = True
    n_odd = False

    if n % 2 != 0:
        n_odd = True
    if n < 0:
        n_pos = False
    if x < 0:
        x_sign = -1
    
    n = abs(n)

    for val in range(1, n+1):
        res = res * x
    
    print("res--->", res)
    
    if n_odd and not n_pos:
        return 1/res
    if n_odd and n_pos:
        return res
    elif not n_odd and not n_pos:
        return 1/res
    elif not n_odd and n_pos:
        return res
    
    return res

print(myPow(0.00001, 2147483647))