def zero_matrix(matrix):
    """Clear columns and rows if a cell contains 0"""

    rows, cols = [], []

    for x in range(len(matrix)): # loop through each inner array
        for y in range(len(matrix[0])): # loop through each element
            if matrix[x][y] == 0: # look for zeroes
                rows.append(x) # add which row the zero is in
                cols.append(y) # add with column the zero is in

    for row in rows: # zero out the appropriate rows
        for i in range(len(matrix)): 
            matrix[row][i] = 0

    for col in cols: #zero out the appropriate columns
        for i in range(len(matrix)):
            matrix[i][col] = 0

    return matrix


print zero_matrix([[1,2,3],[4,0,6],[7,8,9]])