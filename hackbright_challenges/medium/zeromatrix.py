"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    zero_position = None

    # need to get the position of the zero
    for each_list in range(len(matrix)):
        for i in range(len(matrix[each_list])):
            if matrix[each_list][i] == 0: 
                zero_position = (each_list, i)

    # check if the coordinates match the zero position, if so make zero
    for each_list in range(len(matrix)):
        for element in range(len(matrix[each_list])):
            if zero_position and each_list == zero_position[0]:
                matrix[each_list][element] = 0
            if zero_position and element == zero_position[1]:
                matrix[each_list][element] = 0
    return matrix

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
