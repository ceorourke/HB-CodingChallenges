"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    # loop through list
    # if next one is dead, jump 2 spaces
    # if the next one is alive, check next next
        # if next AND next next are alive, jump 2 spaces
    # if next is alive and next next is dead, jump 1 space
    # increment counter each jump
    if len(branches) < 2:
        return 0

    if len(branches) < 3:
        return 1

    count = 0
    branch = 0

    while branch < (len(branches)-1):
        if branches[branch + 1] == 1:
            branch += 2
        else:
            if branches[branch + 2] == 0:
                branch+= 2
            else:
                branch += 1
        count += 1

    return count


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"