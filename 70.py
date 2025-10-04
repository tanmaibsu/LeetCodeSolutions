def climbStairs(n: int) -> int:
    
    if n <= 3: return n
    
    pos1 = 3
    pos2 = 2
    
    curr = 0
    
    for _ in range(3, n):
        curr = pos1 + pos2
        pos2 = pos1
        pos1 = curr
    
    return curr
    
    
    


print(climbStairs(5))