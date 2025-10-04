import numpy as np
def setZeroes(matrix: list[list[int]]):
    """
    Do not return anything, modify matrix in-place instead.
    """

    all_indices = []
    for i, arr in enumerate(matrix):
        indices = [(i, j) for j, elm in enumerate(arr) if elm == 0]
        if indices:
            all_indices.append(indices)
    # return all_indices

    if not indices:
        return matrix
    
    for i, t in enumerate(all_indices[0]):
        print(t)
        matrix[t[0]] = [0] * len(matrix[t[0]])
        for j in range(len(matrix)):
            matrix[j][t[1]] = 0
    
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))