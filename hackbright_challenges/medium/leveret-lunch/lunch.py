"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""
def most_carrots(cells, garden, ncols, nrows):

    legal = [(row, col) for row, col in cells
             if 0 <= row < nrows and 0 <= col < ncols]

    num_carrots = 0
    best = None

    for row, col in legal:
        if num_carrots < garden[row][col]:
            num_carrots = garden[row][col]
            best = row, col

    return best

def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(type(c) is int for c in row for row in garden), \
        "Garden values must be ints!"

    # # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    # # find the middle
    # if (nrows % 2 != 0) and (ncols % 2 != 0):
    #     row = nrows / 2
    #     col = ncols / 2
    #     middle = garden[row][col]
    #     carrots = middle
    #     garden[row][col] = 0
    # else:
    #     # need to find the middle column
    #     if ncols % 2 == 0:
    #         # there are 4 possibilities
    #         middle = max(garden[ncols/2][nrows/2], garden[ncols/2][(nrows/2)+1],
    #                       garden[(ncols/2)+1][nrows/2], garden[(ncols/2)+1][(nrows/2)+1])
    #     else:
    #         # there are 2 possibilities
    #         middle = max(garden[ncols/2][nrows/2], garden[ncols/2][(nrows/2)+1])
 
    # # keep track of how many carrots are eaten, starting with the middle
    # carrots = middle

    # # determine best path for maximum carrots
    # # check WNES, hop to that spot and eat carrots
    # # don't ever go backwards ... so update value to 0?


    # return carrots

    eaten = 0

    consider = [
        ((nrows - 1) / 2, (ncols - 1) / 2),
        ((nrows - 1) / 2, (ncols - 0) / 2),
        ((nrows - 0) / 2, (ncols - 1) / 2),
        ((nrows - 0) / 2, (ncols - 0) / 2)
    ]

    while True:

        # Find row, col coords of cell with most carrots
        curr = most_carrots(consider, garden, ncols, nrows)

        if not curr:
            # We can't find any carrots, so take nap & return
            return eaten

        row, col = curr

        # Eat carrots in that cell and mark it as eaten
        eaten += garden[row][col]
        # print consider, row, col, garden[row][col], eaten
        garden[row][col] = 0

        # Use the WNES neighbors as our next cells to consider.
        # The order here is important --- most_carrots breaks ties
        # by using the first-of-ties, so ensure these are WNES

        consider = [
            (row, col - 1),  # W
            (row - 1, col),  # N
            (row, col + 1),  # E
            (row + 1, col),  # S
        ]


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS! HOP ALONG NOW!\n"
