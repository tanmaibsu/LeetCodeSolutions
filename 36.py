import numpy as np
# import array


def isValidSudoku(board):
        for i, row in enumerate(board):
            row_values = []
            for j, col in enumerate(board):
                if board[i][j] == '.':
                    continue
                else:
                    row_values.append(int(board[i][j]))
            if len(row_values) != len(set(row_values)):
                return False
            else:
                continue
        
        for i in range(9):
            col_values = []
            col_values_b = []
            col_values = [board[j][i] for j in range(len(board))]
            for k in range(len(col_values)):
                if col_values[k] != '.':
                    col_values_b.append(col_values[k])
            # print(col_values_b)
            if len(col_values_b) != len(set(col_values_b)):
                return False
            else:
                continue
        
        sub_arr = (3, 3)
        rows, cols = np.array(board).shape
        partitions = [np.array(board)[i:i+sub_arr[0], j:j+sub_arr[1]] 
              for i in range(0, rows, sub_arr[0]) 
              for j in range(0, cols, sub_arr[1])]

        for idx, sub_a in enumerate(partitions):
            sub_ar = []
            flattened_arr = sub_a.flatten()
            for i, elm in enumerate(flattened_arr):
                if elm != '.':
                    sub_ar.append(elm)
            if len(sub_ar) != len(set(sub_ar)):
                return False
            else:
                continue

        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))