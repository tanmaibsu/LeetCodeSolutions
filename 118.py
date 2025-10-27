def generate(numRows: int) -> list[list[int]]:
    
    tri_arr = []
    tri_arr.append([1])
    
    for i in range(numRows-1):
        sub_arr = []
        sub_arr.append(1)
        
        for j in range(i):
            sub_arr.append(tri_arr[i][j] + tri_arr[i][j+1])
        sub_arr.append(1)
        tri_arr.append(sub_arr)
    return tri_arr 

print(generate(3))

