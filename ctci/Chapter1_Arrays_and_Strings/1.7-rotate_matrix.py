def rotate_matrix(matrix):
    """Rotate a matrix 90 degrees"""

    # first check for valid input
    if (len(matrix) == 0) or (len(matrix) != len(matrix[0])):
        return False

    n = len(matrix)

    for layer in range(n/2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] # save top
            matrix[first][i] = matrix[last - offset][first] # left -> top
            matrix[last - offset][first] = matrix[last][last - offset] # bottom -> left
            matrix[last][last - offset] = matrix[i][last] # right -> bottom
            matrix[i][last] = top # right <- saved top

    return matrix

print rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])